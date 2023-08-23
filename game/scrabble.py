from game.board import Board
from game.player import Player
from game.tiles import BagTiles

class ScrabbleGame:
    def __init__(self, player_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(player_count):
            self.players.append(Player())