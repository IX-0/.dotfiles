#!/bin/sh

echo "Moving .dotfiles to '~/':"

if [[ -d "~/.dotfiles" ]]; then
    echo "ERROR: dot files already exist, exiting..."
    exit 1
else
    mv ../ ~/
    cd ~/.dotfiles/install/
fi

echo "DONE!!!"


echo "Installing yay:"
if [[ ! -x "/sbin/yay" ]]; then
    sudo pacman yay
    [[ $? ]] || echo "ERROR: coudn't install yay" && exit 1
else
    echo "WARNING: yay was already installed, skipping..."
fi

echo "DONE!!!"


echo "Installing packages:"

if [[ -f "~/.dotfiles/install/pkg.txt" ]]; then
    echo "ERROR: no package file found, exiting..."
    exit 1
else
    yay -S $(cat ~/.dotfiles/install/pkg.txt)
    [[ $? ]] || echo "ERROR: something unexpected happened, exiting..." && exit 1
fi

echo "DONE!!!"


echo "Activating ly display manager:"

systemctl enable ly
[[ $? ]] || echo "ERROR: coudn't activate ly dm, exiting..." && exit 1

echo "DONE!!!"


echo "Installing omz!!!"

if [[ -d ~/.oh-my-zsh ]]; then
    echo "WARNING: omz is already installed, skipping..."
else
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" &> /dev/null
    
    [[ $? ]] || echo "ERROR: something unexpected happened, exiting..." && exit 1
    
    sudo rm ~/.zshrc && mv ~/.zshrc.pre-oh-my-zsh ~/.zshrc
fi

echo "Sadly the best part is DONE!!!"


echo "Linking all configs"

sudo ./install/linking.awk ./install.sh/paths.txt 

echo "DONE!!!"
