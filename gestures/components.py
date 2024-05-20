from typing import Callable
import tkinter as tk
from tkhtmlview import HTMLLabel

from gestures import constants

class PreviewFrame(tk.Frame):
    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent, bg=constants.monokai_colors["pink"])
        self.preview_area = HTMLLabel(self, html="<h1>Preview will appear here</h1>",
                                      background=constants.PREVIEW_BACKGROUND,
                                      foreground=constants.PREVIEW_FOREGROUND)
        self.preview_area.pack(fill="both", expand=True)

    def scroll_up(self):
        self.preview_area.yview_scroll(-1, 'units')  # Scroll up

    def scroll_down(self):
        self.preview_area.yview_scroll(1, 'units')  # Scroll down