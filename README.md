# BrainCode Swarm
This repo contains the code for creating swarms for the BrainCode project. 

## Short Intro to the Repo
* **Skills** (under `.claude` or `.agents`; `.claude/` is just a symlink) are for your coding agent to help with creating data in the required format and running swarm scripts.
  Once you open your coding assistant here, it will be aware of the skills and use them when appropriate; you usually don't need to guide it to do that.

* **swarm/** is where the main code is. It contains code for spawning Docker containers where an agent (pi or opencode, for example) runs a *task prompt* on a batch of examples.

* **visualizer/** is a utility code that can help you see visually by simply opening the `visualizer/index.html` file
in your browser and choosing the output folder that the swarm writes to (usually `swarm/output`).

* **vm/** and **vertex-proxy/** are more technical and are not relevant to you. 
