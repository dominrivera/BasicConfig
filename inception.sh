#!/bin/bash

cmd=apt
homedir=~
cd homedir

$cmd update
$cmd upgrade

# Install vim
$cmd install vim

# Remove whitespaces end of line 
echo '\n# Remove whitespaces at end of line \nautocmd BufWritePre * %s/\s\+$//e' >> $homedir/.vimrc

# Install tmux
$cmd install tmux

# Add comment custom configuration
echo '\n###### custom config ######' >> $homedir/.bashrc

# Run tmux by default
echo '\n# Start tmux \n[[ $TERM != \"screen\" ]] && exec tmux' >> $homedir/.bashrc

# Download liquidpromt
git clone https://github.com/nojhan/liquidprompt.git

# Source liquidprompt/liquidprompt
# source liquidprompt/liquidprompt

# Create .liquidpromptrc
cp ~/liquidprompt/liquidpromptrc-dist $homedir/.liquidpromptrc

# Run liquidprompt by default
echo '\n# Only load Liquid Prompt in interactive shells, not from a script or from scp \n[[ $- = *i* ]] && source $homedir/liquidprompt/liquidprompt' >> $homedir/.bashrc

# Start
exec bash