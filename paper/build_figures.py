"""Regenerate manuscript vector figures from saved, unmodified experiment outputs."""
from pathlib import Path
import csv, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'paper/overleaf'
RES = ROOT / 'evaluations/results/main-cov-det'
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':9, 'axes.titlesize':10,
    'axes.labelsize':9, 'xtick.labelsize':8, 'ytick.labelsize':8, 'legend.fontsize':8,
    'pdf.fonttype':42, 'ps.fonttype':42, 'axes.spines.top':False, 'axes.spines.right':False})
def rows(path):
    with open(path,encoding='utf-8-sig',newline='') as f: return list(csv.DictReader(f))
def save(fig,name):
    fig.savefig(OUT/(name+'.pdf'),bbox_inches='tight',pad_inches=.04)
    fig.savefig(ROOT/'paper/reference_review'/(name+'.png'),dpi=160,bbox_inches='tight',pad_inches=.04)
    plt.close(fig)

names=['Gemini 3.7 Flash (high effort)','Gemini 3.7 Flash','Claude Sonnet 5.5','Claude Haiku 4.5','o4-mini']
short=['Flash high','Flash','Sonnet','Haiku','o4-mini']
colors=['#17639a','#59a9c9','#9c4068','#de9360','#6b7280']
datasets=['mind2web','alfred','swebench','prism','paths','thoughttrace']
labels=['Mind2Web','ALFRED','SWE-bench','PRISM','PATHs','ThoughtTrace']
abbr=['M2W','ALF','SWE','PRI','PATH','TT']
cov={r['model']:r for r in rows(RES/'coverage.csv') if r['items']=='shared'}
selfs={r['model']:r for r in rows(RES/'determinism_self.csv') if r['items']=='shared'}

s=rows(ROOT/'swarm/graphs/summary.csv')[1:]
fig,axs=plt.subplots(1,2,figsize=(6.75,1.9),layout='constrained')
dc=['#133f73','#327eb0','#87c5d6','#a14d35','#dc8960','#ebbd85']
for ax,kind,title in zip(axs,['add','refine'],['Proposed additions','Proposed refinements']):
    bottom=np.zeros(len(s))
    for d,l,c in zip(datasets,labels,dc):
        y=np.array([float(r[kind+'_'+d] or 0) for r in s])
        ax.bar(np.arange(1,len(s)+1),y,bottom=bottom,color=c,label=l,width=.85)
        bottom+=y
    ax.set(title=title,xlabel='Development batch',ylabel='Suggestions',xticks=[1,4,7,10,14])
    ax.set_ylim(0,max(bottom)*1.08)
fig.legend(labels,loc='outside upper center',ncol=6,frameon=False,columnspacing=.9)
save(fig,'suggestions')

fig,axs=plt.subplots(1,2,subplot_kw={'projection':'polar'},figsize=(6.75,2.3),layout='constrained')
theta=np.arange(6)*2*np.pi/6
theta=np.r_[theta,theta[0]]
for ax,inds in zip(axs,[[0,1],[2,3]]):
    ax.set_theta_offset(np.pi/2);ax.set_theta_direction(-1)
    for i in inds:
        v=[100*float(cov[names[i]]['success_'+d]) for d in datasets];v.append(v[0])
        ax.plot(theta,v,color=colors[i],label=short[i],lw=1.6,marker='o',ms=3)
    ax.set_xticks(theta[:-1],labels);ax.tick_params(axis='x',pad=5,labelsize=8)
    ax.set_yticks([0,50,100],['0','50','100%']);ax.set_ylim(0,100)
    ax.legend(loc='lower center',bbox_to_anchor=(.5,-.32),ncol=2,frameon=False)
save(fig,'coverage-radar')

matrix=np.zeros((4,4))
for r in rows(RES/'determinism_pairs.csv'):
    if r['model_a'] in names[:4] and r['model_b'] in names[:4]:
        a,b=names.index(r['model_a']),names.index(r['model_b'])
        matrix[a,b]=matrix[b,a]=float(r['js_symbols'])
fig,axs=plt.subplots(1,2,figsize=(6.75,2.3),layout='constrained',gridspec_kw={'width_ratios':[1,1.25]})
ax=axs[0]; ax.imshow(matrix,vmin=0,vmax=.12,cmap='Blues')
ax.set_xticks(range(4),short[:4],rotation=20,ha='right');ax.set_yticks(range(4),short[:4])
ax.set_title('Between-model symbol JS')
for i in range(4):
    for j in range(4):
        ax.text(j,i,f'{matrix[i,j]:.3f}',ha='center',va='center',fontsize=9,color='white' if matrix[i,j]>.075 else 'black')
ax=axs[1]
vals=[float(selfs[n]['self_js_symbols']) for n in names[:4]]
sd=[float(selfs[n]['self_js_symbols_sd']) for n in names[:4]]
ax.barh(range(4),vals,xerr=sd,color=colors[:4],capsize=3)
ax.set_yticks(range(4),short[:4]);ax.invert_yaxis();ax.set_xlim(0,.32)
ax.set(xlabel='Within-item symbol JS (lower is more stable)',title='Self-divergence: mean ± item SD')
for i,v in enumerate(vals):ax.text(.31,i,f'{v:.3f}',ha='right',va='center',fontsize=9)
save(fig,'determinism')

summary=json.loads((RES/'summary.json').read_text())
types=['constructor','value','group_value','attribute','speech_act','operation','claim_relation','other']
tc=['#28608c','#4b95bb','#94c7cd','#e8bb76','#cc7a50','#99515b','#74609b','#b8bdc4']
fig,ax=plt.subplots(figsize=(6.75,1.8),layout='constrained')
left=np.zeros(5)
for ty,c in zip(types,tc):
    vals=[]
    for n in names:
        counts=summary['type_counts'][n]
        v=counts.get(ty,0) if ty!='other' else sum(v for k,v in counts.items() if k not in types)
        vals.append(v/sum(counts.values())*100)
    ax.barh(range(5),vals,left=left,color=c,label=ty.replace('_',' '),height=.7);left+=vals
ax.set_yticks(range(5),short);ax.invert_yaxis();ax.set_xticks([0,25,50,75,100]);ax.set_xlim(0,100)
ax.set_xlabel('Share of recognized symbol occurrences (%)')
fig.legend(loc='outside upper center',ncol=4,frameon=False)
save(fig,'type-mix')

ex=rows(RES/'expressivity.csv')
fig,axs=plt.subplots(1,3,figsize=(6.75,2.0),layout='constrained',sharey=True)
for ax,metric,title in zip(axs,['bleu','rouge_l','word_lev_sim'],['Sentence BLEU','ROUGE-L F1','Word edit similarity']):
    for i in [0,1]:
        data={r['dataset']:float(r[metric]) for r in ex if r['model']==names[i] and r['items']=='all'}
        ax.plot(range(6),[data[l] for l in labels],marker='o',ms=3,lw=1.4,color=colors[i],label=short[i])
    ax.set(title=title,xticks=range(6),xticklabels=abbr,ylim=(0,.65))
    ax.tick_params(axis='x',labelrotation=40);ax.grid(axis='y',alpha=.18)
axs[0].set_ylabel('Reconstruction score (higher is better)')
fig.legend(['Flash high','Flash'],loc='outside upper center',ncol=2,frameon=False)
save(fig,'expressivity')

fig,axs=plt.subplots(1,2,figsize=(6.75,2.7),layout='constrained')
for i,n in enumerate(names):
    x=float(cov[n]['success_rate'])*100;y=float(selfs[n]['self_js_symbols'])
    axs[0].scatter(x,y,c=colors[i],s=45)
    dx=-5 if i in [0,3] else 5
    dy=-11 if i in [0,3] else 5
    axs[0].annotate(short[i],(x,y),xytext=(dx,dy),textcoords='offset points',ha='right' if dx<0 else 'left',fontsize=8)
    vals=[float(selfs[n]['self_js_'+d]) for d in datasets]
    axs[1].plot(range(6),vals,color=colors[i],label=short[i],marker='o',ms=3)
axs[0].set(xlim=(0,102),ylim=(0,.4),xlabel='Coverage (%)',ylabel='Self-divergence (lower is better)')
axs[1].set(xticks=range(6),xticklabels=abbr,ylim=(0,.5),ylabel='Self-divergence by dataset')
axs[1].tick_params(axis='x',labelrotation=35)
fig.legend(short,loc='outside upper center',ncol=5,frameon=False)
save(fig,'appendix-determinism')

# Exact all-task counts and rates, drawn from the saved individual runs.
ir=rows(ROOT/'evaluations/improvement/results/improvement_runs.csv')
tasks=sorted(set(r['task'] for r in ir))
lines=[]
for task in tasks:
    groups=[[r for r in ir if r['task']==task and r['condition']==c] for c in ['baseline','braincode']]
    if not groups[1]: groups[1]=[r for r in ir if r['task']==task and r['condition']!='baseline']
    n=len(groups[0]);a=sum(int(r['correct']) for r in groups[0]);b=sum(int(r['correct']) for r in groups[1])
    lines.append(f'{task.title()} & {n} & {a} ({100*a/n:.1f}) & {b} ({100*b/n:.1f}) \\\\')
(OUT/'improvement-rows.tex').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Created 6 vector chart files and all 23 task rows; the pipeline diagram is in main.tex.')
