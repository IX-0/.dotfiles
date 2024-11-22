#----------------------------
#OMZ and ZSH conf
#----------------------------

# Path to omz installation.
export ZSH="$HOME/.oh-my-zsh"

#ZSH theme
ZSH_THEME="powerlevel10k/powerlevel10k" 

#Update rules
zstyle ':omz:update' mode auto
zstyle ':omz:update' frequency 1

#Command correction
#ENABLE_CORRECTION="true"

plugins=(git)
source $ZSH/oh-my-zsh.sh

#----------------------------
#ENV VARIABLES
#----------------------------
export EDITOR="nvim"
export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH:.

#----------------------------
#ALIASES
#----------------------------
alias ll="ls -al"
alias la="ls -a"
alias cls="clear"
alias kys="systemctl poweroff"
alias lendariocla="ssh xs@lendariocla.duckdns.org"
alias llendariocla="ssh xs@192.168.1.51"
alias nm="nmtui"
alias blth="bluetui"
alias rnvim="sudo -Es nvim"
alias rnv="rnvim"
alias nv="nvim"
alias ff="fastfetch"  
alias rq="kys"
alias cat="bat"

#----------------------------
#ON STARTUP
#----------------------------
eval "$(zoxide init zsh)" #Start zoxide
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh # p10k config setup
ff # I use arch btw
