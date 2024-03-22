from constants import *
from buttons import *
import tkinter  as tk
try:
    from ctypes import windll, byref, c_int, sizeof
except:
    pass

class Calculator(tk.Tk):
    def __init__(self):

        super().__init__()
        self.config(bg= WHITE)
        self.title('Calculator App')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)
        self.title_bar_color()


        #layout
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')

        #data
        self.result_string = tk.StringVar(value="0")
        self.formula_string = tk.StringVar(value='')
        self.display_nums = []
        self.full_operation = []

        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        #fonts
        main_font = (FONT, NORMAL_FONT_SIZE)
        result_font = (FONT, OUTPUT_FONT_SIZE)

        #output labels
        OutputLabel(self, 0, 'se', main_font, self.formula_string)
        OutputLabel(self, 1, 'e', result_font, self.result_string)

        #buttons
        Button(
            parent = self, 
            func = self.clear,
            text = OPERATORS['clear']['character'],
            col = OPERATORS['clear']['col'],
            row = OPERATORS['clear']['row'],
            font = main_font
        )

        Button(
            parent = self, 
            func = self.percent,
            text = OPERATORS['percent']['character'],
            col = OPERATORS['percent']['col'],
            row = OPERATORS['percent']['row'],
            font = main_font
        )
        
        Button(
            parent= self, 
            func = self.invert,
            text = OPERATORS['invert']['character'],
            col = OPERATORS['invert']['col'],
            row = OPERATORS['invert']['row'],
            font = main_font
        )

        #num buttons
        for num, data in NUM_POSITIONS.items():
            NumButton(
                parent = self,
                text = num,
                func = self.num_press,
                col = data['col'],
                row = data['row'],
                font = main_font, 
                span = data['span'] 
            )

        for operator, data in MATH_POSITIONS.items():

            MathButton(
            parent = self,
            text = data['character'],
            operator = operator, 
            func = self.math_press,
            col = data['col'],
            row = data['row'],
            font = main_font
        )

    def title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMA_attribute = 35
            COLOR = TITLE_BAR_HEX_COLORS
            windll.dwmapi.DWMSetWindowAttribute(HWND, DWMA_attribute, byref(c_int(COLOR)), sizeof(c_int))

        except:
            pass


    def num_press(self, value):
        self.display_nums.append(value)
        full_number = ''.join(self.display_nums)
        self.result_string.set(full_number)

    def math_press(self, value):
        current_number = ''.join(self.display_nums)

        if current_number:
            self.full_operation.append(current_number)

            if value != '=':
                self.full_operation.append(value)
                self.display_nums.clear()

                self.result_string.set('')
                self.formula_string.set(' '.join(self.full_operation))
            else:
                formula = ''.join(self.full_operation)
                result = eval(formula)

                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)

                self.full_operation.clear()
                self.display_nums = [str(result)]

                self.result_string.set(result)
                self.formula_string.set(formula)


    def clear(self):
        self.result_string.set(0)
        self.formula_string.set('')

        self.display_nums.clear()
        self.full_operation.clear()

    def percent(self):
        if self.display_nums:
            current_number = float("".join(self.display_nums))
            percent_number = current_number / 100

            self.display_nums = list(str(percent_number))
            self.result_string.set(''.join(self.display_nums))


    def invert(self):
        current_number = ''.join(self.display_nums)
        if current_number:
            if float(current_number) > 0:
                self.display_nums.insert(0, '-')

            else:
                del self.display_nums[0]

            self.result_string.set(''.join(self.display_nums))
            

class OutputLabel(tk.Label):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master = parent, font = font, textvariable = string_var)
        self.grid(column = 0, row = row, columnspan = MAIN_COLUMNS, sticky = anchor, padx = 10)


if __name__ == '__main__':
    Calculator()
