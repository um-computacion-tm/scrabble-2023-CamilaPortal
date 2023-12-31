from game.cell import Cell
from game.tiles import Tile
from game.player import Player

TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2),
                    (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11),
                        (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'L': 1, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1,
    'P': 3, 'Q': 5, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Y': 4, 'Z': 10
}

class SoloVoHParaLaOrientacion(Exception):
    pass

class WordOutOfBoard(Exception):
    pass

class NotEnoughLetters(Exception):
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

    def set_cell_multiplier(self, coordinate, multiplier_type, multiplier):
        cell = self.grid[coordinate[0]][coordinate[1]]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier
    
    def set_multipliers(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.set_cell_multiplier(coordinate, "word", 3)
        for coordinate in DOUBLE_WORD_SCORE:
            self.set_cell_multiplier(coordinate, "word", 2)
        for coordinate in TRIPLE_LETTER_SCORE:
            self.set_cell_multiplier(coordinate, "letter", 3)
        for coordinate in DOUBLE_LETTER_SCORE:
            self.set_cell_multiplier(coordinate, "letter", 2)

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
        if orientation.upper() == "H":
            return self.validate_word_horizontal(word, location)
        elif orientation.upper() == "V":
            return self.validate_word_vertical(word, location)
        else:
            raise SoloVoHParaLaOrientacion(Exception)
        
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        return False

    def can_place_word_at_start(self, x, y, word):
        if y <= 7 < y + len(word) and x == 7:
            return True
        return False

    def validate_word_place_board_horizontal(self, word, location):
        x, y = location
        if not self.validate_word_inside_board(word, location, "H"):
            raise WordOutOfBoard(Exception)
        if self.is_empty():
            return self.can_place_word_at_start(x, y, word)
        elif self.is_empty() is False:
            for i in range(len(word)):
                if self.grid[x][y + i].letter is not None:
                    if self.grid[x][y + i].letter.letter != word[i]:
                        return False
            return True

    def validate_word_place_board_vertical(self, word, location):
        x, y = location
        if not self.validate_word_inside_board(word, location, "V"):
            raise WordOutOfBoard(Exception)
        if self.is_empty():
            return self.can_place_word_at_start(y, x, word)
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
        
    # def put_word(self, word, location, orientation):
    #     x, y = location
    #     cells = []
    #     for i, letter in enumerate(word):
    #         if orientation.upper() == 'H':
    #             cell= self.grid[x][y + i]
    #         elif orientation.upper() == 'V':
    #             cell=self.grid[x + i][y]
            
    #         value = values.get(letter, 0)
    #         tile = Tile(letter=letter, value=value)
    #         cell.add_letter(tile)
    #         cells.append(cell)
    #     return cells

    def put_word(self, word, location, orientation, player_tiles):
        x, y = location
        cells = []
        for i, letter in enumerate(word):
            if orientation.upper() == 'H':
                cell = self.grid[x][y + i]
            elif orientation.upper() == 'V':
                cell = self.grid[x + i][y]
            
            # Buscar la letra en las fichas del jugador
            tile = next((t for t in player_tiles if t.letter == letter), None)
            if tile:
                value = tile.value
            else:
                value = 0  # Asignar un valor predeterminado si la letra no está en las fichas del jugador
            
            cell.add_letter(Tile(letter=letter, value=value))
            cells.append(cell)
        
        # Actualizar la lista de fichas del jugador después de jugar la palabra
        for letter in word:
            tile_to_remove = next((t for t in player_tiles if t.letter == letter), None)
            if tile_to_remove:
                player_tiles.remove(tile_to_remove)
        
        return cells
            
    def get_word_cells(self, word, location, orientation):
        word_cells = [] 
        row, col = location 

        for letter in word:
            word_cells.append(self.grid[row][col])  
            if orientation.upper() == 'H':
                col += 1  
            elif orientation.upper()=='V':
                row += 1  
        return word_cells
    
    @staticmethod
    def calculate_word_value(word: list[Cell]) -> int:
        value: int = 0
        multiplier_word = None

        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
                cell.active == False
        if multiplier_word:
            value = value * multiplier_word
        return value
        
                
    def has_adjacent_horizontal_letter(self, x, y):
        return (y - 1 >= 0 and self.grid[x][y - 1].letter is not None) or (y + 1 < 15 and self.grid[x][y + 1].letter is not None)

    def has_adjacent_vertical_letter(self, x, y):
        return (x - 1 >= 0 and self.grid[x - 1][y].letter is not None) or (x + 1 < 15 and self.grid[x + 1][y].letter is not None)


    def is_valid_crossword(self, word, location, orientation):
        x, y = location
        for i, letter in enumerate(word):
            if orientation.lower() == 'h':
                if self.has_adjacent_horizontal_letter(x, y + i):
                    return True
            elif orientation.lower() == 'v':
                if self.has_adjacent_vertical_letter(x + i, y):
                    return True
        return False
    






