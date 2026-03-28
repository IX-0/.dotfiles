from libqtile import widget, qtile
from libqtile.command.base import expose_command
from theme import theme

POWER_PROFILES = {
    "balanced-battery": "󰖨 ",
    "powersave": " ",
    "throughput-performance": "⚡",
}

class IconTunedManager(widget.TunedManager):
    def __init__(self, **config):
        super().__init__(**config)
        self.current_mode = "unknown" # Initialize to avoid early access error

    def custom_text(self):
        return POWER_PROFILES.get(self.current_mode, self.current_mode)

    def find_mode(self):
        import re, subprocess
        try:
            result = subprocess.run("tuned-adm active", shell=True, capture_output=True, text=True, timeout=2)
            combined = result.stdout + result.stderr
            match = re.search(r"Current active profile:\s+(\S+)", combined)
            return match.group(1) if match else "unknown"
        except Exception:
            return "unknown"

    def _configure(self, qtile, bar):
        super()._configure(qtile, bar)
        self.current_mode = self.find_mode()
        self.text = self.custom_text()

    def poll(self):
        self.current_mode = self.find_mode()
        return self.custom_text()

    @expose_command()
    def update_widget(self):
        self.current_mode = self.find_mode()
        self.text = self.custom_text()
        self.bar.draw()

class CustomGroupBox(widget.GroupBox):
    def draw(self):
        self.drawer.clear(self.background or self.bar.background)

        offset = self.margin_x
        for i, g in enumerate(self.groups):
            to_highlight = False
            is_block = self.highlight_method == "block"
            is_line = self.highlight_method == "line"

            bw = self.box_width([g])

            if self.group_has_urgent(g) and self.urgent_alert_method == "text":
                text_color = self.urgent_text
            elif g.screen:
                if self.highlight_method == "text":
                    if g.screen == self.qtile.screens[0]:
                        text_color = theme.fg_grey1
                    elif len(self.qtile.screens) > 1 and g.screen == self.qtile.screens[1]:
                        text_color = theme.green
                    else:
                        text_color = self.this_current_screen_border
                else:
                    text_color = self.active
            elif g.windows:
                text_color = self.active
            else:
                text_color = self.inactive

            if g.screen and self.highlight_method != "text":
                if self.block_highlight_text_color:
                    text_color = self.block_highlight_text_color
                if self.bar.screen.group.name == g.name:
                    if self.qtile.current_screen == self.bar.screen:
                        border = self.this_current_screen_border
                        to_highlight = True
                    else:
                        border = self.this_screen_border
                else:
                    if self.qtile.current_screen == g.screen:
                        border = self.other_current_screen_border
                    else:
                        border = self.other_screen_border
            elif self.group_has_urgent(g) and self.urgent_alert_method != "text":
                border = self.urgent_border
                if self.urgent_alert_method == "block":
                    is_block = True
                elif self.urgent_alert_method == "line":
                    is_line = True
            else:
                border = None

            self.drawbox(
                offset,
                g.label,
                border,
                text_color,
                highlight_color=self.highlight_color,
                width=bw,
                rounded=self.rounded,
                block=is_block,
                line=is_line,
                highlighted=to_highlight,
            )
            offset += bw + self.spacing
        self.draw_at_default_position()
