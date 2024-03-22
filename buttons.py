from constants import *
import tkinter  as tk
import tkinter.ttk as ttk

class Button(tk.Button):
    def __init__(self, parent, func, col, row, font, text, color = 'dark-gray'):
        super().__init__(
            master = parent,
            text = text, 
            command = func, 
            font = font,
            background = COLORS[color]['bg'],
            foreground = COLORS[color]['text'])
        self.grid(column = col, row = row, sticky = 'nsew', padx = STYLING['gap'], pady = STYLING['gap'])

class NumButton(Button):
    def __init__(self, parent, func, col, row, font, span, text, color = 'light-gray'):
        super().__init__(
            parent = parent,
            text = text, 
            func = lambda: func(text) , 
            col = col,
            row = row,
            color = color,
            font = font,
            )
        self.grid(column = col, columnspan = span, row = row, sticky = 'nsew', padx = STYLING['gap'], pady = STYLING['gap'])

class MathButton(Button):
    def __init__(self, parent, operator, func, col, row, font, text, color = 'orange'):
        super().__init__(
            parent = parent,
            text = text, 
            func = lambda: func(operator), 
            col = col,
            row = row,
            color = color,
            font = font,
            )

