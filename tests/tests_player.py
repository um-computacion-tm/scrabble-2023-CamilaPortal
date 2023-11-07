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
        bag_tiles = BagTiles()
        player = Player(bag_tiles)
        player.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        word = 'HOLA'
        result = player.has_letters(word)
        self.assertTrue(result)
        self.assertEqual(len(player.tiles), 3)
    
    def test_has_not_letters(self):
        bag_tiles = BagTiles()
        player = Player(bag_tiles)
        player.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        word = 'GOOD'
        result = player.has_letters(word)
        self.assertFalse(result)

    def test_has_letters_with_duplicate_letters(self):
        bag_tiles = BagTiles()
        player = Player(bag_tiles)
        player.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='B', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='D', value=1),
        ]
        word = 'BAD'
        result = player.has_letters(word)
        self.assertTrue(result)

    def test_has_letters_with_insufficient_duplicate_letters(self):
        bag_tiles = BagTiles()
        player = Player(bag_tiles)
        player.tiles = [
            Tile(letter='G', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='D', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        word = 'GOOD'
        result = player.has_letters(word)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()