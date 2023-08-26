from game.tiles import Tile

class Cell:
    def __init__(self, multiplier, multiplier_type):

        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

    def add_letter(self, letter: Tile):
        self.letter= letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
    def calculate_word_value(self, cells):
        total_value = 0
        word_multiplier = 1

        for cell in cells:
            cell_value = cell.calculate_value()
            if cell.multiplier_type == 'word':
                word_multiplier *= cell.multiplier
            total_value += cell_value

        return total_value * word_multiplier