from game.cell import Cell

class SoloVoHParaLaOrientacion(Exception):
    pass

class Board:
    def __init__(self):
        self.grid=[
            [Cell(1, '') for _ in range (15)]
            for _ in range (15)
        ]

        self.set_multipliers()

    def set_multiplier(self, row, col, multiplier_type, multiplier):
        self.grid[row][col].multiplier_type = multiplier_type
        self.grid[row][col].multiplier = multiplier
    
    def set_multipliers(self):
        self.set_multiplier(0, 0, 'word', 3)
        self.set_multiplier(0, 3, 'letter', 2)
        self.set_multiplier(0, 7, 'word', 3)
        self.set_multiplier(0, 11, 'letter', 2)
        self.set_multiplier(0, 14, 'word', 3)

    def validate_word_inside_board(self, word, location, orientation):
        x, y = location
        if orientation == "H":
            if x < 0 or x >= 15 or y < 0 or y + len(word) > 15:
                return False
        elif orientation == "V":
            if x < 0 or x + len(word) > 15 or y < 0 or y >= 15:
                return False
        else:
            raise SoloVoHParaLaOrientacion(Exception)

        return True
