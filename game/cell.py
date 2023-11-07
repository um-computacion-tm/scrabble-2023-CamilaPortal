from game.tiles import Tile

values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'L': 1, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1,
    'P': 3, 'Q': 5, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Y': 4, 'Z': 10, '*':0
}

class Cell:
    def __init__(self, multiplier=1, multiplier_type="", letter=None, active=True):

        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active

    def add_letter(self, letter: Tile):
        self.letter= letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            result = values.get(self.letter.letter) * self.multiplier
            self.multiplier_type = None
            self.active = False
            return result
        else:
            return values.get(self.letter.letter, 0)
        
    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '
        
    