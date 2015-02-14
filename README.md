# HATS Simulator

This repository contains the current code for the simulator being built for the ECEX574 HATS Project.

# Contributing

The approach outlined below is a current proposed approach to contributing. This document is a living document, and subject to updates and improvements based on the teams' feedback and suggestions. Team members are encouraged to discuss the current approach, suggest improvements, identify pain points, etc. This approach is initially based on several factors - GitHub's [suggestions](https://help.github.com/articles/using-pull-requests/) for collaboration, ZeroMQ's [treatise](http://zguide.zeromq.org/page:all#toc130) on building strong development communities, and personal experience with working on large, fast-paced projects. That doesn't mean it's bulletproof - just that there's some background material generating all this.

## Submitting Code

In order to contribute to this project, we are going to use the [Pull Request](https://help.github.com/articles/using-pull-requests/) model favored by GitHub and many other modern version control systems. This means you do not directly commit or push to the master branch of the main repository. The general development model should happen as follows:

1. Create your local working directory, either by forking the repo, or by creating a branch off master.
2. Once you have some body of work which you believe is ready to be part of the master branch, issue a Pull Request on the main repository.
3. Someone else on the team will be assigned to review the pull request. This will be assigned randomly, to ensure we share the reviewing load and become familiar with all aspects of the system. The person who submitted the Pull Request shall not accept the Pull Request, nor be assigned to review their own work.
4. Please respond to feedback until the reviewer makes a final decision on the Pull Request. This process in based on group consensus and collaboration - while a Pull Request can be rejected if it doesn't meet the guidelines of the project, everyone should make reasonable effort to help Pull Requests meet our guidelines and get integrated as quickly as possible.

## Reviewing Code

When assigned to a Pull Request, you should be aiming to read through the code to understand what the Pull Request is trying to do, and if it meets our guidelines for submission. The guidelines are meant to address high level issues:

1. A Pull Request should address one explicit and logical change to the codebase.
2. A Pull Request should only include code which meets the coding guidelines.
3. A Pull Request should allow the system to run, and pass any unit tests which are included in the code-base. No breaking the build in master.
4. A Pull Request should have commit messages should be concise, descriptive summarizations of the changes in the commit.
5. A Pull Request should contain code which meets the Honoe Code of Virginia Tech. No plagiarism, attribute work to the actual developer of said code, etc.

## Coding Guidelines

For Python code, code in this project should adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/), the Python Codeing Guidelines.