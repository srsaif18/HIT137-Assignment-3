import tkinter as tk
from tkinter import ttk


class StatusBar(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="No image loaded yet", anchor="w")
        self.pack(side=tk.BOTTOM, fill=tk.X)

    def update_status(self, text):
        self.config(text=text)
