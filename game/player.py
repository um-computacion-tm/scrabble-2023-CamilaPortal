from game.tiles import BagTiles

class Player:

    def __init__(self, bag_tiles):
        self.tiles = bag_tiles.take(7)
        self.bag_tiles = bag_tiles
    
    def rellenar(self):
        self.tiles += self.bag_tiles.take(7 - len(self.tiles))

    def has_letters(self, tiles):
        tiles_counts = {tile.letter: tile.value for tile in tiles}
        player_tiles_counts = {tile.letter: tile.value for tile in self.tiles}

        for letter, count in tiles_counts.items():
            if letter not in player_tiles_counts or count > player_tiles_counts[letter]:
                return False
        return True
