from libqtile import layout
from theme import theme

lay_config = {
    "border_width": 2,
    "margin": 9,
    "border_focus": theme.green,
    "border_normal": theme.fg_grey1,
    "font": "JetBrainsMono Nerd Font",
    "grow_amount": 10,
}

layouts = [
    layout.Columns(
        **lay_config,
        border_on_single=True,
        num_columns=2,
        split=True,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
