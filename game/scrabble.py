from game.board import Board
from game.player import Player
from game.tiles import BagTiles

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for index in range(players_count):
            self.players.append(Player(index + 1, self.bag_tiles))

        
        self.current_player = None
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player= self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player=self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]
    
    def is_playing(self):
        return True
    
    def get_current_player(self):
        return self.current_player, self.players
    
    def get_board(self):
        return self.board
    
    # def play(self, word, location, orientation):
    #     self.validate_word(word, location, orientation)
    #     words=self.board.put_word(word, location, orientation)
    #     total = calculate_words_value(words)
    #     self.players[self.current_player].score += total
    #     self.next_turn()

    # def next_turn(self):
    #     self.current_player = (self.current_player + 1)% len(self.players)
    
    # def validate_word(self, word, location, orientaiton):
    #     if not dict_validate_word(word):         dictionary.py
    #         raise InvalidWord("no existe")
    #     if not self.board.validate_word_inside_board(word, location, orientaiton):
    #         raise InvalidPlaceWordException("ii")
    #     if not self.board.validate_word_place_board(word, location, orientaiton):
    #         raise InvalidPlaceWordException("")

    # def change(self, letters):
    #     self.get_current_player().take_tile_using_letters(letters)

    # def play(self, word, location, orientation):
    #     missing_lettes = self.validate_word(word, location, orientation)
    #     words= self.board.put_word(word, location, orientation, self.get_current_player())
    #     total=calculate_words_value(words)
    #     self.get_current_player().fill()
    #     self.get_current_player().score +=total
    #     self.next_turn()