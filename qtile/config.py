from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

# C O N S T A N T S
mod = "mod4"
terminal = "alacritty"
keyboards = ["pt","us"]
fileManager = "thunar" 

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█
# K E Y B I N D S

keys = [

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("sh -c ~/.config/rofi/scripts/launcher"), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "r", lazy.spawn("sh -c ~/.config/rofi/scripts/run") ,desc="rofi run"),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='powermenu'),
    Key([mod],"e", lazy.spawn(fileManager), desc='file manager'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    Key([], "XF86PowerOff", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='powermenu via power button'),
    Key([mod, "shift"], "XF86PowerOff", lazy.spawn("systemctl poweroff"))
]

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█



groups = [Group(f"{i+1}", label="") for i in range(5)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )

# L A Y O U T S


lay_config = {
    "border_width": 2,
    "margin": 9,
    "border_focus": "#A7C080",
    "border_normal": "#86918A",
    "font": "JetBrainsMono Nerd Font",
    "grow_amount": 10,
}

layouts = [
    # layout.MonadWide(**lay_config),
    layout.Columns(
        **lay_config,
        border_on_single=True,
        num_columns=2,
        split=True,
    ),
    # Plasma(lay_config, border_normal_fixed='#3b4252', border_focus_fixed='#3b4252', border_width_single=3),
    # layout.RatioTile(**lay_config),
    # layout.VerticalTile(**lay_config),
    # layout.Matrix(**lay_config, columns=3),
    # layout.Zoomy(**lay_config),
    # layout.Slice(**lay_config, width=1920, fallback=layout.TreeTab(), match=Match(wm_class="joplin"), side="right"),
    # layout.MonadTall(**lay_config),
    # layout.Tile(shift_windows=True, **lay_config),
    # layout.Stack(num_stacks=2, **lay_config),
    # layout.Floating(**lay_config),
    # layout.Max(**lay_config),
]



widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = [ widget_defaults.copy() ]


def search():
    qtile.spawn("sh -c ~/.config/rofi/scripts/launcher")

def power():
    qtile.spawn("sh -c ~/.config/rofi/scripts/power")


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄



screens = [
    #Main screen
    Screen(
        top=bar.Bar(
            [
                
                widget.Spacer(length=15,
                    background='#232A2E',
                ),

                widget.KeyboardLayout(
                    configured_keyboards = keyboards,
                    background = "#232A2E",
                    foreground = '#86918A',
                    font = "JetBrainsMono Nerd Font Bold",
                    fontsize = 13,
                    borderwidth = 3,
                ),

                widget.Spacer(length=8,
                    background='#232A2E',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#232A2E',
                    mouse_callbacks={"Button1": power},
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),

                widget.GroupBox(
                    font="JetBrainsMono Nerd Font",
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active='#86918A',
                    block_highlight_text_color="#D3C6AA",
                    highlight_color='#4B427E',
                    inactive='#232A2E',
                    foreground='#4B427E',
                    background='#343F44',
                    this_current_screen_border='#343F44',
                    this_screen_border='#343F44',
                    other_current_screen_border='#343F44',
                    other_screen_border='#343F44',
                    urgent_border='#343F44',
                    rounded=True,
                    disable_drag=True,
                ),

                widget.Spacer(
                    length=8,
                    background='#343F44',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),

                widget.CurrentLayout(
                    custom_icon_paths=["~/.dotfiles/qtile/Assets/layout"],
                    background='#343F44',
                    mode="icon",
                    scale=0.5,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),

                widget.TextBox(
                    text="",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background='#232A2E',
                    foreground='#86918A',
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background='#232A2E',
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    foreground='#86918A',
                    mouse_callbacks={"Button1": search},
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),

                widget.WindowName(
                    background='#343F44',
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    empty_group_string="Desktop",
                    max_chars=130,
                    foreground='#86918A',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),

                widget.Systray(
                    background='#232A2E',
                    fontsize=2,
                ),

                widget.TextBox(
                    text=' ',
                    background='#232A2E',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#343F44',
                ),
                
                widget.TextBox(
                    text="",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background='#343F44',
                    foreground='#86918A',
                ),

                widget.Wlan( # Needs python-iwlib
                    format="{essid} {percent:2.0%}",
                    background = "#343f44",
                    font = "JetBrainsMono Nerd Font Bold",
                    fontsize = 13,
                    foreground = "#86918a",
                    padding = 3,
                    update_interval = 3
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#343F44',
                ),

                widget.TextBox(
                    text="",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background='#343F44',
                    foreground='#86918A',
                ),

                widget.Memory(
                    background='#343F44',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#86918A',
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    update_interval=5,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#343F44',
                ),

                widget.TextBox(
                    text=" ",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background='#343F44',
                    foreground='#86918A',
                ),

                widget.Battery(
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    background='#343F44',
                    foreground='#86918A',
                    format='{percent:2.0%}',
                    low_foreground='#DBBC7F"',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#343F44',
                ),

                widget.TextBox(
                    text=" ",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background='#343F44',
                    foreground='#86918A',
                ),

                widget.PulseVolume(  # Needs pulsectl_asyncio
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    background="#343F44",
                    foreground="#86918A",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("pavucontrol")
                    },
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#343F44',
                ),

                widget.TextBox(
                    text=" ",
                    font="Font Awesome 7 Free Solid",
                    fontsize=13,
                    background='#232A2E',
                    foreground='#86918A',
                ),

                widget.Clock(
                    format='%I:%M %p',
                    background='#232A2E',
                    foreground='#86918A',
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                ),

                widget.Spacer(
                    length=18,
                    background='#232A2E',
                ),

            ],
            30,
            border_color='#86918A',
            border_width=[0,0,0,0],
            margin=[15,9,6,9],
        ),
    ),

    #Secondary Screen
    Screen()
]

# O P T I O N S

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser('.config/qtile/autostart_once.sh')])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
# E O F
