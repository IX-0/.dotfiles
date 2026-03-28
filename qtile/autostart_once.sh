#!/bin/zsh

# Turn off hdmi output
xrandr --output HDMI-1-0 --off

# Start picom
picom --config ~/.config/picom/picom.conf &

# Start network-applet
nm-applet &

# Start blueman-applet 
blueman-applet &

# Start redshift
redshift -l 40.72974:-8.4815 &

# Start dunst
dunst &
sleep 3 && bash ~/.dotfiles/dunst/welcome.sh &
bash ~/.dotfiles/dunst/log_monitor.sh &
