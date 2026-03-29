from dataclasses import dataclass

@dataclass
class Theme:
    # --- Foreground colors ---
    fg:             str = "#D3C6AA"  # default foreground, text
    fg_grey0:       str = "#7A8478"  # darkest grey, subtle text
    fg_grey1:       str = "#859289"  # mid grey, inactive/secondary text
    fg_grey2:       str = "#9DA9A0"  # lightest grey, dimmed text

    # --- Accent colors ---
    white:          str = "#FFFFFF"  # just white
    red:            str = "#E67E80"  # errors, urgent, warnings
    orange:         str = "#E69875"  # special highlights
    yellow:         str = "#DBBC7F"  # warnings, low battery
    green:          str = "#A7C080"  # focused, active, success
    aqua:           str = "#83C092"  # other screen active, secondary success
    blue:           str = "#7FBBB3"  # info
    purple:         str = "#D699B6"  # misc

    # --- Background colors ---
    bg_dim:         str = "#232A2E"  # darkest bg, outermost bar sections
    bg0:            str = "#2D353B"  # default window background
    bg1:            str = "#343F44"  # raised elements, inner bar sections
    bg2:            str = "#3D484D"  # subtle borders, separators
    bg3:            str = "#475258"  # cursor line, color columns
    bg4:            str = "#4F585E"  # non-text elements
    bg5:            str = "#56635F"  # borders

    # --- Semantic background accents ---
    bg_red:         str = "#514045"  # red tinted background
    bg_yellow:      str = "#4D4C43"  # yellow tinted background
    bg_green:       str = "#425047"  # green tinted background
    bg_blue:        str = "#3A515D"  # blue tinted background
    bg_purple:      str = "#4A444E"  # purple tinted background
    bg_visual:      str = "#543A48"  # visual selection background

    # --- Statusline roles ---
    statusline1:    str = "#A7C080"  # active statusline (same as green)
    statusline2:    str = "#D3C6AA"  # middle statusline (same as fg)
    statusline3:    str = "#E67E80"  # urgent statusline (same as red)

theme = Theme()
