from game.tiles import BagTiles
from game.tiles import Tile

class Player:

    def __init__(self,player_index,bag_tiles=BagTiles()):
        self.player_index = player_index
        self.tiles = bag_tiles.take(7)
        self.bag_tiles = bag_tiles
    
    def rellenar(self):  #fill
        self.tiles += self.bag_tiles.take(7 - len(self.tiles))

    def has_letters(self, word):
        word_tiles_counts = {letter: word.count(letter) for letter in word}
        player_tiles_counts = {tile.letter: self.tiles.count(tile) for tile in self.tiles}

        for letter, count in word_tiles_counts.items():
            if letter not in player_tiles_counts or count > player_tiles_counts[letter]:
                return False
        return True
    
    def __str__(self):
        return f"{self.player_index}"
    
    #def take_tile_using_letters()
