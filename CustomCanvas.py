import tkinter as tk
from tkinter import Canvas

class CustomCanvas:
    def __init__(self, height: int, width: int):
        self.window = tk.Tk()
        self.canvas = Canvas(self.window, width=width, height=height)

    def draw_rectangle(self, rect):
        self.canvas.create_rectangle(
            rect.x, rect.y, rect.x + rect.width, rect.y + rect.height,
            outline='black', fill='blue'
        )

    def display(self):
        self.canvas.pack()
        self.window.mainloop()
