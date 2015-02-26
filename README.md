# HATS Simulator

This repository contains the current code for the simulator being built for the ECEX574 HATS Project.

# Installing

This software should run on both Mac OS X and Windows. In order to get the software up and running, you must complete the following steps:

1. Install [Python](https://www.python.org/), the latest version 2.7 version.
2. Install [GraphViz](http://graphviz.org/). Note: If you are using a Mac, you may already be using [Homebrew](http://brew.sh/), which is significantly simpler to install this tool.
3. Use pip to install `pygraphviz numpy pyparsing pyyaml networkx`
4. Clone the repository to your computer. Assuming you will be cloning the code to `~/src/hats_sim`, the cloning command will be something along the lines of `git clone git@github.com:jasedit/hats_sim.git ~/src/hats_sim`.
  1. Note: If you haven't set up SSH keys with GitHub, you should instead use `git clone https://github.com/jasedit/hats_sim.git ~/src/hats_sim` to make it work. But you should set up SSH keys with GitHub.
5. Modify your `~/.bash_profile` file to add hats_sim to your PYTHONPATH. Add the line `export PYTHONPATH=$PYTHONPATH:${HOME}/src/hats_sim`

# Contributing

Please read CONTRIBUTING.md for instructions on how to contribute to this repository.