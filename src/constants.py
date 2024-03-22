APP_SIZE = (400,700)
MAIN_ROWS = 7
MAIN_COLUMNS = 4

FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32

STYLING = {
    'gap': 0.5}

NUM_POSITIONS = {
    '.' : {'col': 2, 'row': 6, 'span': 1},
    '0' : {'col': 0, 'row': 6, 'span': 2},
    '1' : {'col': 0, 'row': 5, 'span': 1},
    '2' : {'col': 1, 'row': 5, 'span': 1},
    '3' : {'col': 2, 'row': 5, 'span': 1},
    '4' : {'col': 0, 'row': 4, 'span': 1},
    '5' : {'col': 1, 'row': 4, 'span': 1},
    '6' : {'col': 2, 'row': 4, 'span': 1},
    '7' : {'col': 0, 'row': 3, 'span': 1},
    '8' : {'col': 1, 'row': 3, 'span': 1},
    '9' : {'col': 2, 'row': 3, 'span': 1}}

MATH_POSITIONS = {
    '/': {'col': 3, 'row': 2, 'character': '/'},
    '*': {'col': 3, 'row': 3, 'character': 'X'},
    '-': {'col': 3, 'row': 4, 'character': '-'},
    '=': {'col': 3, 'row': 6, 'character': '='},
    '+': {'col': 3, 'row': 5, 'character': '+'}
}

OPERATORS = {
    'clear': {'col': 0, 'row': 2, 'character': 'AC'},
    'invert': {'col': 1, 'row': 2, 'character': '+/-'},
    'percent': {'col': 2, 'row': 2, 'character': '%'}
}
COLORS = {
    'light-gray': {'bg': '#505050', 'text':'WHITE'},
    'dark-gray': {'bg': '#D4D4D2', 'text': 'BLACK'},
    'orange': {'bg': '#FF9500', 'text': 'BLACK'},
}

TITLE_BAR_HEX_COLORS = 0x00EEEEEE

WHITE = '#EEEEEE'