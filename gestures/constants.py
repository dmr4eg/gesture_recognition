"""Colors, fonts, and other constants used by the interface."""

import colorsys


def darken_color(hex_color_str, factor=0.8):
    """Darken a color by multiplying its RGB values by the given factor."""
    hex_color_str = hex_color_str.strip("#")
    r, g, b = [int(hex_color_str[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)

    l *= factor
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    darker_hex_color_str = "".join([f"{int(255 * c):02x}" for c in (r, g, b)])

    return "#" + darker_hex_color_str


DEFAULT_WINDOW_SIZE = "1000x600"

PREVIEW_BACKGROUND = "white"
PREVIEW_FOREGROUND = "black"

EDITOR_FONT = "monospace"
EDITOR_FONT_SIZE = 12

monokai_colors = {
    "green": "#A6E22E",
    "cyan": "#66D9EF",
    "foreground": "#F8F8F2",
    "pink": "#F92672",
    "yellow": "#E6DB74",
    "background": "#282923",
    "gray": "#74705d",
    "blue": "#67d8ef",
    "orange": "#fd9621",
    "purple": "#ac80ff",
    "red": "#f83535"
}

EXPLORER_BACKGROUND = darken_color(monokai_colors["background"])
EXPLORER_FOREGROUND = monokai_colors["foreground"]

custom_monokai = {
    "editor": {
        "bg": monokai_colors["background"],
        "fg": monokai_colors["foreground"],
        "select_bg": "#48473d",
        "select_fg": monokai_colors["foreground"],
        "inactive_select_bg": "#48473d",
        "caret": monokai_colors["foreground"],
        "caret_width": 1,
        "border_width": 0,
        "focus_border_width": 0
    },
    "general": {
        "comment": monokai_colors["gray"],
        "error": monokai_colors["pink"],
        "escape": monokai_colors["foreground"],
        "keyword": monokai_colors["pink"],
        "name": monokai_colors["green"],
        "string": monokai_colors["yellow"],
        "punctuation": monokai_colors["pink"]
    },
    "keyword": {
        "constant": monokai_colors["purple"],
        "declaration": monokai_colors["pink"],
        "namespace": monokai_colors["pink"],
        "pseudo": monokai_colors["purple"],
        "reserved": monokai_colors["pink"],
        "type": monokai_colors["pink"]
    },
    "name": {
        "attr": monokai_colors["green"],
        "builtin": monokai_colors["blue"],
        "builtin_pseudo": monokai_colors["orange"],
        "class": monokai_colors["green"],
        "class_variable": monokai_colors["green"],
        "constant": monokai_colors["foreground"],
        "decorator": monokai_colors["blue"],
        "entity": monokai_colors["green"],
        "exception": monokai_colors["blue"],
        "function": monokai_colors["green"],
        "global_variable": monokai_colors["green"],
        "instance_variable": monokai_colors["green"],
        "label": monokai_colors["green"],
        "magic_function": monokai_colors["blue"],
        "magic_variable": monokai_colors["green"],
        "namespace": monokai_colors["foreground"],
        "tag": monokai_colors["pink"],
        "variable": monokai_colors["pink"]
    },
    "operator": {
        "symbol": monokai_colors["red"],
        "word": monokai_colors["pink"]
    },
    "string": {
        "affix": monokai_colors["yellow"],
        "char": monokai_colors["yellow"],
        "delimiter": monokai_colors["yellow"],
        "doc": monokai_colors["yellow"],
        "double": monokai_colors["yellow"],
        "escape": monokai_colors["yellow"],
        "heredoc": monokai_colors["yellow"],
        "interpol": monokai_colors["yellow"],
        "regex": monokai_colors["yellow"],
        "single": monokai_colors["yellow"],
        "symbol": monokai_colors["yellow"]
    },
    "number": {
        "binary": monokai_colors["purple"],
        "float": monokai_colors["purple"],
        "hex": monokai_colors["purple"],
        "integer": monokai_colors["purple"],
        "long": monokai_colors["purple"],
        "octal": monokai_colors["purple"]
    },
    "comment": {
        "hashbang": monokai_colors["gray"],
        "multiline": monokai_colors["gray"],
        "preproc": monokai_colors["pink"],
        "preprocfile": monokai_colors["yellow"],
        "single": monokai_colors["gray"],
        "special": monokai_colors["gray"]
    },
    "generic": {
        "heading": monokai_colors["green"],
        "subheading": monokai_colors["cyan"],
        "emph": monokai_colors["foreground"],
        "strong": monokai_colors["pink"],
        "deleted": monokai_colors["pink"]
    }
}
