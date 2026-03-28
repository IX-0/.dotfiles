import os
from libqtile import bar, widget, qtile
from libqtile.lazy import lazy
from libqtile.config import Screen
from theme import theme
from widgets.custom import IconTunedManager, CustomGroupBox, POWER_PROFILES
from constants import keyboards

@lazy.function
def search(qtile):
    qtile.spawn("sh -c ~/.dotfiles/rofi/scripts/launcher")

@lazy.function
def power(qtile):
    qtile.spawn("sh -c ~/.dotfiles/rofi/scripts/power")

@lazy.function
def tuned_picker(qtile):
    qtile.spawn("bash -c 'DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus bash ~/.dotfiles/rofi/scripts/tuned_picker'")

# Wallpaper path
wallpaper_path = os.path.expanduser("~/.dotfiles/assets/wallpaper.jpg")

screens = [
    #Main screen
    Screen(
        wallpaper=wallpaper_path,
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(length=15,
                    background=theme.bg_dim,
                ),

                widget.KeyboardLayout(
                    configured_keyboards = keyboards,
                    background = theme.bg_dim,
                    foreground = theme.fg_grey1,
                    font = "JetBrainsMono Nerd Font Bold",
                    fontsize = 13,
                    borderwidth = 3,
                ),

                widget.Spacer(length=8,
                    background=theme.bg_dim,
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/launch_Icon.png',
                    margin=2,
                    background=theme.bg_dim,
                    mouse_callbacks={"Button1": power},
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/6.png',
                ),

                CustomGroupBox(
                    font="JetBrainsMono Nerd Font",
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='text',
                    active=theme.fg_grey1, # Light Gray for groups with windows
                    block_highlight_text_color=theme.fg,
                    highlight_color=theme.bg_purple,
                    inactive=theme.bg_dim,
                    foreground=theme.bg_purple,
                    background=theme.bg1,
                    this_current_screen_border=theme.green, # Everforest Green for focused group
                    this_screen_border=theme.bg1,
                    other_current_screen_border=theme.aqua, # Everforest Aqua (Other Screen)
                    other_screen_border=theme.bg1,
                    urgent_border=theme.red, # Everforest Red
                    rounded=True,
                    disable_drag=True,
                ),

                widget.Spacer(
                    length=8,
                    background=theme.bg1,
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/1.png',
                ),

                widget.CurrentLayout(
                    custom_icon_paths=[os.path.expanduser("~/.dotfiles/assets/layout")],
                    background=theme.bg1,
                    mode="icon",
                    scale=0.5,
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/5.png',
                ),

                widget.TextBox(
                    text="",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background=theme.bg_dim,
                    foreground=theme.fg_grey1,
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background=theme.bg_dim,
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    foreground=theme.fg_grey1,
                    mouse_callbacks={"Button1": search},
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/4.png',
                ),

                widget.WindowName(
                    background=theme.bg1,
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    empty_group_string="Desktop",
                    max_chars=130,
                    foreground=theme.fg_grey1,
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/3.png',
                ),

                widget.Systray(
                    background=theme.bg_dim,
                    fontsize=2,
                ),

                widget.TextBox(
                    text=' ',
                    background=theme.bg_dim,
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/6.png',
                    background=theme.bg1,
                ),
                
                widget.TextBox(
                    text="",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background=theme.bg1,
                    foreground=theme.fg_grey1,
                ),

                widget.Wlan( # Needs python-iwlib
                    format="{essid} {percent:2.0%}",
                    background = theme.bg1,
                    font = "JetBrainsMono Nerd Font Bold",
                    fontsize = 13,
                    foreground = theme.fg_grey1,
                    padding = 3,
                    update_interval = 3
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background=theme.bg1,
                ),

                widget.TextBox(
                    text="",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background=theme.bg1,
                    foreground=theme.fg_grey1,
                ),

                widget.Memory(
                    background=theme.bg1,
                    format='{MemUsed: .0f}{mm}',
                    foreground=theme.fg_grey1,
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    update_interval=5,
                ),
                
                widget.Image(
                    filename='~/.dotfiles/assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background=theme.bg1,
                ),

                IconTunedManager(
                    background=theme.bg1,
                    foreground=theme.fg_grey1,
                    font="JetBrainsMono Nerd Font Bold",
                    modes=list(map(lambda k: str(k), POWER_PROFILES.keys())),
                    update_interval=3600,
                    name="tuned",
                    fontsize=15,
                    mouse_callbacks={
                        "Button1": tuned_picker
                    },
                ),

                widget.Battery(
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    background=theme.bg1,
                    foreground=theme.fg_grey1,
                    format='{percent:2.0%}',
                    low_foreground=theme.yellow,
                    charging_foreground=theme.green,
                    mouse_callbacks={
                        "Button1": tuned_picker
                    },
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background=theme.bg1,
                ), 

                widget.TextBox(
                    text=" ",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background=theme.bg1,
                    foreground=theme.fg_grey1,
                    mouse_callbacks={
                        "Button1": lambda: qtile.spawn("pavucontrol")
                    },

                ),

                widget.PulseVolume(  # Needs pulsectl_asyncio
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    background=theme.bg1,
                    foreground=theme.fg_grey1,
                    mouse_callbacks={
                        "Button1": lambda: qtile.spawn("pavucontrol")
                    },
                ),

                widget.Image(
                    filename='~/.dotfiles/assets/5.png',
                    background=theme.bg1,
                ),

                widget.Clock(
                    format='%d-%m-%Y  %I:%M %p',
                    background=theme.bg_dim,
                    foreground=theme.fg_grey1,
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                ),

                widget.Spacer(
                    length=18,
                    background=theme.bg_dim,
                ),

            ],
            30,
            border_color=theme.fg_grey1,
            border_width=[0,0,0,0],
            margin=[15,9,6,9],
        ),
    ),

    Screen(
        wallpaper=wallpaper_path,
        wallpaper_mode="fill",
    ),
]
