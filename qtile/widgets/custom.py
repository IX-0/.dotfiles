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
            bw = self.box_width([g])

            if self.group_has_urgent(g):
                text_color = self.urgent_border
            elif g.screen:
                if self.bar.screen == g.screen:
                    text_color = self.this_current_screen_border
                else:
                    text_color = self.other_current_screen_border
            elif g.windows:
                text_color = self.active
            else:
                text_color = self.inactive

            self.drawbox(
                offset,
                g.label,
                None, # No border
                text_color,
                highlight_color=self.highlight_color,
                width=bw,
                rounded=self.rounded,
                block=False,
                line=False,
                highlighted=False,
            )
            offset += bw + self.spacing
        self.draw_at_default_position()
