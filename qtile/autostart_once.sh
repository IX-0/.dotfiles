#!/bin/zsh

# Apply wallpaper using wal
wal -b 232A2E -i ~/.config/qtile/Assets/wallpaper.jpg &&

# Start picom
picom --config ~/.config/picom/picom.conf &
