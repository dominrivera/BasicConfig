#!/usr/bin/python

import os

cmd = "apt"
homedir = os.path.expanduser("~")
os.chdir(homedir)

os.system("%s upgrade" % cmd)
os.system("%s update" % cmd)

# Install vim
os.system("%s install vim" % cmd)
#install tmux
os.system("%s install tmux" % cmd)
# Add comment custom configuration
os.system("echo '\n###### custom config ######' >> ~/.bashrc")
# Run tmux by default
os.system("echo '\n# Start tmux \n[[ $TERM != \"screen\" ]] && exec tmux' >> ~/.bashrc")
# Download liquidpromt
os.system("git clone https://github.com/nojhan/liquidprompt.git")
# Source liquidprompt/liquidprompt
#os.system("source liquidprompt/liquidprompt")
# Create .liquidpromptrc
os.system("cp ~/liquidprompt/liquidpromptrc-dist ~/.liquidpromptrc")
# Run liquidprompt by default
os.system("echo '\n# Only load Liquid Prompt in interactive shells, not from a script or from scp \n[[ $- = *i* ]] && source ~/liquidprompt/liquidprompt' >> ~/.bashrc")
os.system("exec bash")
#os.system("")
#os.system("")
#os.system("")
#os.system("")
