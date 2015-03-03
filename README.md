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

# Running the simulator

1. Execute `./hats_sim/sim.py ./config/config.yaml` from the root directory

# Using the device hub simulator

The simulator includes a basic simulator for an abstract device hub. It is an extension of the built-in Python HTTPServer class.
The device hub simulator maintains a dictionary of Device objects (see device.py). It will respond to a GET request by attempting to find a device in that dictionary with a key that matches the request path, and returning the result of a toJson call on that object. It responds to POST requests by reading the request body as JSON and attempting to update a device matching the request path with that dictionary.

The device hub simulator implementation can (and should) be modified or overridden to simulate the behavior of an actual API for some actual device hub, but until that API is firmly specified it can serve as a stand-in that at least allows you to verify that API calls to devices are being made.

Running the device_hub_server.py file starts the server listening on port 8080, and adds a couple of device objects to it as a demo. It can be halted by pressing CTRL+C. You may modify the code to set up a more complex demo.

# Contributing

Please read CONTRIBUTING.md for instructions on how to contribute to this repository.
