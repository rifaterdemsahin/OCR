#!/bin/bash

# Test SSH connection to GitHub and clone a public repository
ssh -T git@github.com && git clone git@github.com:octocat/Hello-World.git
