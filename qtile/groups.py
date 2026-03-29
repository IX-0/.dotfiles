from libqtile.config import Group, Key
from libqtile.lazy import lazy
from keys import keys
from constants import mod

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
                    lazy.window.togroup(i.name, switch_group=False),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )
