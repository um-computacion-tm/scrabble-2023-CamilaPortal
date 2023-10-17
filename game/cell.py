from game.tiles import Tile

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
        if self.multiplier_type == 'letter' and self.active:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
    def calculate_word_value(self, cells):
        total_value = 0
        word_multiplier = 1

        for cell in cells:
            cell_value = cell.calculate_value()
            if cell.multiplier_type == 'word' and cell.active:
                word_multiplier *= cell.multiplier
            total_value += cell_value

        return total_value * word_multiplier

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '
        
    