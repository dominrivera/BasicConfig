#!/usr/bin/python

import os

os.system("cd")
os.system("apt upgrade")
os.system("apt update")

# Install vim
os.system("apt install vim")
# Install git
os.system("apt install git")
#install tmux
os.system("apt install tmux")
# Add comment custom configuration
os.system("echo '\n###### custom config ######' >> ~/.bashrc")
# Run tmux by default
os.system("echo '\n# Start tmux \n[[ $TERM != \"screen\" ]] && exec tmux' >> ~/.bashrc")
# Download liquidpromt
os.system("git clone https://github.com/nojhan/liquidprompt.git")
# Source liquidprompt/liquidprompt
os.system("source liquidprompt/liquidprompt")
# Create .liquidpromptrc
os.system("cp ~/liquidprompt/liquidpromptrc-dist ~/.liquidpromptrc")
# Run liquidprompt by default
os.system("echo '# Only load Liquid Prompt in interactive shells, not from a script or from scp \n[[ $- = *i* ]] && source ~/liquidprompt/liquidprompt' >> ~/.bashrc")
#os.system("")
#os.system("")
#os.system("")
#os.system("")
#os.system("")
