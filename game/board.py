from game.cell import Cell
from game.tiles import Tile

class SoloVoHParaLaOrientacion(Exception):
    pass

class NoValid(Exception):
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
    

    def validate_word_horizontal(self, word, location):
        x, y = location
        if x < 0 or x >= 15 or y < 0 or y + len(word) > 15:
            return False
        return True

    def validate_word_vertical(self, word, location):
        x, y = location
        if x < 0 or x + len(word) > 15 or y < 0 or y >= 15:
            return False
        return True

    def validate_word_inside_board(self, word, location, orientation):
        if orientation == "H":
            return self.validate_word_horizontal(word, location)
        elif orientation == "V":
            return self.validate_word_vertical(word, location)
        else:
            raise SoloVoHParaLaOrientacion(Exception)
        
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        return False

    def validate_word_place_board_horizontal(self, word, location):
        x, y = location
        if not self.validate_word_inside_board(word, location, "H"):
            return False
        if self.is_empty() is True:
            if y <= 7 < y + len(word) and x == 7:
                return True
            return False
        elif self.is_empty() is False:
            for i in range(len(word)):
                if self.grid[x][y + i].letter is not None:
                    if self.grid[x][y + i].letter.letter != word[i]:
                        return False
            return True

    def validate_word_place_board_vertical(self, word, location):
        x, y = location
        if not self.validate_word_inside_board(word, location, "V"):
            return False
        if self.is_empty() is True:
            if x <= 7 < x + len(word) and y == 7:
                return True
            return False
        elif self.is_empty() is False:
            for i in range(len(word)):
                if self.grid[x + i][y].letter is not None:
                    if self.grid[x + i][y].letter.letter != word[i]:
                        return False
            return True

    def validate_word_place_board(self, word, location, orientation):
        if orientation == "H":
            return self.validate_word_place_board_horizontal(word, location)
        elif orientation == "V":
            return self.validate_word_place_board_vertical(word, location)
        else:
            raise SoloVoHParaLaOrientacion(Exception)
        
    def put_word(self, word, location, orientation):
        if self.validate_word_inside_board(word, location, orientation) and self.validate_word_place_board(word, location, orientation):
            x, y = location
            if orientation.lower() == 'h':
                for i, letter in enumerate(word):
                    tile = Tile(letter, value=any)  
                    self.grid[x][y + i].letter = tile
            elif orientation.lower() == 'v':
                for i, letter in enumerate(word):
                    tile = Tile(letter, value=any)
                    self.grid[x + i][y].letter = tile
        else:
            raise NoValid(Exception)




