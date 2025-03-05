#!/bin/zsh

# Apply wallpaper using wal
wal -b 232A2E -i ~/.config/qtile/Assets/wallpaper.jpg &&

# Start picom
picom --config ~/.config/picom/picom.conf &

# Start network-applet
nm-applet &

# Start blueman-applet 
blueman-applet &

# Start redshift
redshift -l 40.72974:-8.4815 &
