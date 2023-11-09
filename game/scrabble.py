from game.board import Board
from game.player import Player
from game.tiles import BagTiles, Tile
from game.cell import Cell
from game.dictionary import validate_word as validate_word_dict

class InvalidWord(Exception):
    pass

class InvalidPlaceWordException(Exception):
    pass

class NoJoker(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.player= Player()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player(bag_tiles=self.bag_tiles))   
        self.current_player = 0

    def next_turn(self):
        self.current_player = (self.current_player + 1)% len(self.players)
    
    def is_playing(self):
        return True
    
    def get_current_player(self):
        return self.players[self.current_player]
    
    def get_player_tiles(self):
        return self.players[self.current_player].tiles
    
    def get_board(self):
        return self.board
        
    def validate_word(self, word, location, orientation):
        word = word.upper()
        if not validate_word_dict(word):
            raise InvalidWord("No existe la palabra")
        elif not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("No es correcta la ubicación")
        elif not self.board.is_empty():
            if not self.board.is_valid_crossword(word, location, orientation):
                raise InvalidPlaceWordException("La palabra debe estar cruzada")
        elif not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("No se puede colocar")
        
    def convert_joker_to_letter(self, letter):
        current_player = self.get_current_player()
        current_player.convert_joker(letter)

    def get_joker_index(self):
        joker_indices = [index for index, tile in enumerate(self.get_current_player().tiles) if tile.letter == '*']
        if joker_indices:
            return joker_indices[0]
        else:
            raise NoJoker("No tiene joker")
        
    def play(self, word, location, orientation, rack):

        self.validate_word(word, location, orientation)
        self.get_current_player().has_letters(word)
        self.board.put_word(word, location, orientation, rack)
        word_cells = self.board.get_word_cells(word, location, orientation) 
        total_score = self.board.calculate_word_value(word_cells)
        self.players[self.current_player].score += total_score
        self.players[self.current_player].rellenar()
        self.next_turn()

    def compare_score(self):
        max_score = 0
        max_score_players = []

        for player in self.players:
            if player.score > max_score:
                max_score = player.score
                max_score_players = [player]
            elif player.score == max_score:
                max_score_players.append(player)

        return max_score_players
    
    def finish_game(self):
        if len(self.bag_tiles.tiles) == 0:
            return True
        return False
