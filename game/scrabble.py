from game.board import Board
from game.player import Player
from game.tiles import BagTiles
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