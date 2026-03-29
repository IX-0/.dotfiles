from libqtile.config import Key
from libqtile.lazy import lazy
from constants import mod, alt, terminal, fileManager

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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "m", lazy.spawn("lxrandr")),
    Key([mod], "t", lazy.spawn("nwg-look"), desc="Launch LXAppearance"),
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

@lazy.function
def next_active_group(qtile):
    current_index = int(qtile.current_group.name) - 1
    
    for i in range(1, len(qtile.groups)):
        nxt = qtile.groups[(current_index + i) % len(qtile.groups)]
        if nxt.windows:
            qtile.current_screen.set_group(nxt)
            break

keys.append(Key(["mod1"], "Tab", next_active_group))
