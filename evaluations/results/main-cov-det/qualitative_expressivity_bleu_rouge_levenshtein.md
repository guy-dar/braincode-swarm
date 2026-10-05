# Qualitative analysis: expressivity (BLEU / ROUGE-L / word-Levenshtein round trip), written by claude-opus-5-5

# Qualitative analysis of BrainCode round-trip differences

## 1. Types of differences

The evidence covers 99 round-trip pairs: 46 for Gemini 3.7 Flash, 46 for Gemini 3.7 Flash (high effort) and 7 for o4-mini. The difference types below are ordered roughly by frequency.

**(a) Compression / summarisation (the dominant effect).**
- Between 54% and 71% of pairs per model are flagged as compressed.
- Mean length ratios are 0.36–0.67.
- Expansion is rare (0–4.3%).

Long assistant turns are reduced to short, flat propositions:
- prism-4 (Flash): a multi-sentence answer on marriage becomes *"A person's commitment to a partner is important. However, this varies with personal values. Marriage enables fulfillment."*
- paths-3 (high effort, length ratio 0.14): a full medieval *Inception* plot becomes a list of entities, e.g. *"Johnathon Wyrd and Lady Elyria."* and *"Elara, Silas, and Caelum."*

An extreme form replaces content with a description of the content:
- o4-mini, prism-1: *"The assistant provides detailed information about work-life balance policies and outcomes in Japan."*
- o4-mini, prism-1, next assistant turn: *"Understood—you want information about multiple part-time jobs in Japan."*
- o4-mini, mind2web-3: the assistant turn is empty (*"<|assistant|>"*), so all five UI actions are lost.

**(b) Lexical paraphrase and normalisation.** Even when content survives, wording is regularised. Examples:
- *"Head forward to the bed in front of you"* → *"Walk in front of the bed"*
- *"book"* → *"textbook"*
- *"night stand"* → *"nightstand"*
- *"Cool the lettuce"* → *"Chill the lettuce"*
- *"cell phone"* → *"phone"*

User questions are recast into a canonical "What is…" form:
- *"how important do you think marriage is"* → *"What is the importance of marriage?"*
- *"i would like to know how to mow my lawn"* → *"What are the instructions for mowing a lawn?"*

Register and formatting are flattened as well:
- *"Hell yeah, let's plan this trip! 🔥"* disappears in thoughttrace-2.
- Markdown headers and emoji vanish.

**(c) Step and turn restructuring.**
- *Steps* differ in 50–71% of pairs per model. Numbered lists become prose, and steps are split or merged. For example, ALFRED *"3. Turn to your right and walk to the night stand"* becomes *"Turn right. Walk to the nightstand."*
- Mind2Web action syntax *"[link] Tabs -> CLICK"* is verbalised as *"Click "Tabs""*.
- *Turns* are mostly preserved (13% differ for both Gemini variants, 28.6% for o4-mini), with three exceptions:
  - ALFRED reconstructions drop the chat frame entirely (2 → 0 turns), along with the user's goal (*"Read a book by lamp light"* is gone).
  - o4-mini collapses prism-3 from 6 turns to 2.
  - Flash duplicates an assistant turn in prism-4 (*"I am unaware whether marriage is outdated…"* appears twice).

**(d) Loss or distortion of specifics.** The mean shares lost per model are:

| | numbers lost | names lost | identifiers lost |
|---|---|---|---|
| Range across models | 0.53–0.90 | 0.43–0.73 | 0.50–0.69 |

Examples:
- *"You are so tall I am 5'5""* → *"The character has a height of tall"* (paths-7).
- The Flash/high-effort ALFRED pair differs only in whether the title survives: Flash drops *"the book that says Probabilistic Robotics"*, high effort keeps it.

Some "losses" are transformations rather than deletions:
- *"no more than a third"* → *"at most 33.3333333333%"* (prism-2).
- *"We only use it in one place"* → *"There is 1 duplicate definition"* (swebench-7). Here the meaning changes too.

Some quantities appear to be distorted or invented:
- *"long work hours of 1 hour in Japan"* (prism-1, high effort).
- *"For narrative writing, 1 works best."* (thoughttrace-1, Flash).

**(e) Additions and glossary leakage.** Added-word shares are 0.21–0.26 per model. Three kinds of addition are visible:
- *Formal-language symbols surface as English text*, typically snake_case tokens:
  - *"unique_accounts_tied_to_ssn_or_id"*
  - *"story_bible"*, *"character_profiles"*
  - *"romantic_interest"*, *"online_setting"*
  - *"build_type" is "cross_build"*
- *Relational templates produce nonsense*:
  - *"Notion provides Obsidian. Google Docs provides Trello."*
  - *"Reducing criminal fraud enables high infrastructure investment."* (a user turn rendered as a causal claim)
- *Framing phrases* such as *"I propose modifying…"*, *"Here is the story:"*.

**(f) Meaning reversal.** The clearest case is o4-mini on prism-3: *"Why **doesn't** the government eliminate anonymous online activities…"* → *"Why **does** the government eliminate…"*. The assistant turn then asserts the opposite: *"The government eliminates anonymous online activities…"*.

**(g) Language switch.** Language switches occur in 6.5–14% of pairs per model. The only verified case is thoughttrace-1, where a French conversation comes back in English (*"Bonjour ! Je souhaiterais ton aide…"* → *"Hello. I need help."*). The high-effort run partly keeps the French, copying the heading *"Guide d'Organisation pour ta Fanfiction"* verbatim.

## 2. Per model

| | pairs | ROUGE-L | BLEU | Lev | len. ratio | compressed | steps diff | turns diff | numbers lost | names lost | identifiers lost | added |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 3.7 Flash | 46 | .355 | .103 | .242 | .58 | 65% | 57% | 13% | .67 | .46 | .69 | .21 |
| Gemini 3.7 Flash (high effort) | 46 | .380 | .114 | .275 | .67 | 54% | 50% | 13% | .53 | .43 | .69 | .22 |
| o4-mini | 7 | .267 | .082 | .170 | .36 | 71% | 71% | 29% | .90 | .73 | .50 | .26 |

**Gemini 3.7 Flash vs. high effort.**
- Higher effort mainly *reduces compression*. Length ratio rises from .58 to .67, and the compressed share falls from 65% to 54%.
- It *keeps more numbers*: numbers lost drops from .67 to .53.
- Names (.46 → .43) and identifiers (.69 in both) barely move, and the added-word rate is unchanged (~.22).
- The gains are therefore about *retaining more*, not about adding less or paraphras
