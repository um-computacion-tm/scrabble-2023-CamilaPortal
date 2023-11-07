from game.tiles import BagTiles
from game.tiles import Tile

class Player:

    def __init__(self, bag_tiles=BagTiles()):
        self.bag_tiles = BagTiles() 
        self.tiles = bag_tiles.take(7)
        self.score = 0
    
    def rellenar(self):
        self.tiles += self.bag_tiles.take(7 - len(self.tiles))

    def has_letters(self, word):
        player_tiles = self.tiles.copy()
        word_letters_counts = {letter: word.count(letter) for letter in word}
        
        for letter, count in word_letters_counts.items():
            found_tiles = [tile for tile in player_tiles if tile.letter == letter]
            if len(found_tiles) < count:
                return False
            
            for _ in range(count):
                player_tiles.remove(found_tiles.pop(0))
        
        self.tiles = player_tiles
        
        return True
    
    
    #def take_tile_using_letters()
