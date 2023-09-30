import unittest
from game.player import Player
from game.tiles import Tile, BagTiles

class TestPlayer(unittest.TestCase):

    def test_init(self):
        bag_tile = BagTiles()
    
        player_1= Player(bag_tile)
        self.assertEqual(
            len(player_1.tiles), 7
        )
    
    def test_rellenar(self):
        bag_tiles = BagTiles()
        player = Player(bag_tiles)
        
        player.rellenar()
        tiles = player.tiles
        
        self.assertEqual(len(tiles), 7)


    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile('H', 1),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1),
            Tile('M', 1),
            Tile('O', 1),
            Tile('G', 1),
        ]
        player_1 = Player(bag_tile)
        tiles = [
            Tile('H', 1),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1)
        ]

        is_valid = player_1.has_letters(tiles)

        self.assertEqual(is_valid, True)
    
    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.has_letters(tiles)

        self.assertEqual(is_valid, False)


if __name__ == '__main__':
    unittest.main()