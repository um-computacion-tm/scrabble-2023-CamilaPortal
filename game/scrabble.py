from game.board import Board
from game.player import Player
from game.tiles import BagTiles, Tile
from game.cell import Cell
from game.dictionary import validate_word as validate_word_dict

class InvalidWord(Exception):
    pass

class InvalidPlaceWordException(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player( self.bag_tiles))
    
        self.current_player = 0

    def next_turn(self):
        self.current_player = (self.current_player + 1)% len(self.players)
    
    def is_playing(self):
        return True
    
    def get_current_player(self):
        return self.players[self.current_player]
    
    def get_board(self):
        return self.board
    
        
    def validate_word(self, word, location, orientaiton):
        if not validate_word_dict(word):
            raise InvalidWord("No existe la palabra")
        if not self.board.validate_word_inside_board(word, location, orientaiton):
            raise InvalidPlaceWordException("No es correcta la ubicación")
        if not self.board.validate_word_place_board(word, location, orientaiton):
            raise InvalidPlaceWordException("No se puede colocar")
    
    def get_tile_value(self, letter):
        for tile in self.bag_tiles.tiles:
            if tile.letter == letter:
                return tile.value
        return 0
    
    def get_coordinates_for_index(self, location, orientation, index):
        x, y = location
        if orientation.lower() == 'h':
            return x, y + index
        elif orientation.lower() == 'v':
            return x + index, y
        else:
            raise ValueError("Orientación no válida")
    
    def get_score(self, word, location, orientation):
        total_score = 0
        word_multiplier = 1

        for i, letter in enumerate(word.upper()):
            row, col = self.get_coordinates_for_index(location, orientation, i)
            tile_value = self.get_tile_value(letter)

            cell = self.board.grid[row][col]

            if cell.active:
                cell = Cell(letter=Tile(letter, tile_value),
                            multiplier_type=cell.multiplier_type,
                            multiplier=cell.multiplier)
                cell_value = cell.calculate_value()
                total_score += cell_value

                if cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier

        return total_score * word_multiplier
        
    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        self.board.put_word(word, location, orientation)
        total_score = self.get_score(word, location, orientation)

        self.players[self.current_player].rellenar()
        self.players[self.current_player].score += total_score

        x, y = location
        for i in range(len(word)):
            if orientation == 'H':
                self.board.deactivate_cell(x, y + i)
            else:
                self.board.deactivate_cell(x + i, y)
        self.next_turn()

    
    # def play(self, word, location, orientation):
    #     self.validate_word(word, location, orientation)
    #     words=self.board.put_word(word, location, orientation)
    #     total = calculate_words_value(words)
    #     self.players[self.current_player].score += total
    #     self.next_turn()


    # def change(self, letters):
    #     self.get_current_player().take_tile_using_letters(letters)

    # def play(self, word, location, orientation):
    #     missing_lettes = self.validate_word(word, location, orientation)
    #     words= self.board.put_word(word, location, orientation, self.get_current_player())
    #     total=calculate_words_value(words)
    #     self.get_current_player().fill()
    #     self.get_current_player().score +=total
    #     self.next_turn()