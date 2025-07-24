#!/bin/zsh

#----------------------------
#OMZ and ZSH conf
#----------------------------

# Enable Powerlevel10k instant prompt. 
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to omz installation.
export ZSH="$HOME/.oh-my-zsh"

# Path to omz custom plugins
export ZSH_CUSTOM="$HOME/.dotfiles/omz_custom"

#ZSH theme
ZSH_THEME="powerlevel10k/powerlevel10k" 

#Update rules
zstyle ':omz:update' mode auto
zstyle ':omz:update' frequency 1

#Command correction
#ENABLE_CORRECTION="true"

plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh

#----------------------------
#ENV VARIABLES
#----------------------------
export EDITOR="nvim"
export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH:.

#ANTLR4
export CLASSPATH=".:/usr/local/lib/antlr-4.13.2-complete.jar:/usr/local/lib/ST-4.3.4.jar"
export ANTLR4_PATH="/usr/local/lib"

#----------------------------
#ALIASES
#----------------------------
alias ll="ls -al"
alias la="ls -a"
alias cls="clear"
alias kys="systemctl poweroff"
alias lendariocla="ssh daisy@lendariocla.duckdns.org"
alias llendariocla="ssh daisy@192.168.1.51"
alias nm="nmtui"
alias nv="nvim"
alias rq="kys"
alias cat="bat"

#ANTLR4
ANTLR4="antlr4"
alias a4-b="antlr4-build"
alias a4-c="antlr4-clean"
alias a4-r="antlr4-run"


#----------------------------
#FUNCTIONS
#----------------------------

pyenv() {
    if [[ -f bin/activate ]] ; then
        source bin/activate &> /dev/null
    elif [[ -f .venv/bin/activate ]]; then
        source .venv/bin/activate &> /dev/null
    elif [[ -f .env/bin/activate ]]; then
        source .venv/bin/activate &> /dev/null
    else
        echo "No venv found"
    fi
}

ff ()
{
    clear
    fastfetch $*
}

zvim ()
{
    z $1 &> /dev/null
    if [[ $? -ne 0 ]]; then
        echo "No zoxide entries for '$1'"
        return 1
    fi
    nvim
}

yayclean ()
{
    yay -Qdtq | yay -Rns -
}

#----------------------------
#ON STARTUP
#----------------------------
eval "$(zoxide init zsh)" #Start zoxide
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh # p10k config setup
#ff # I use arch btw
