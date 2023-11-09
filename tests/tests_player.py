import unittest
from game.player import Player, NoJoker
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
        self.assertEqual(len(player.tiles), 7)

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

    def test_joker_in_tiles(self):
        bag_tiles=BagTiles()
        player= Player(bag_tiles)
        player.tiles = [Tile('A', 1), Tile('B', 1), Tile('*', 0), Tile('D', 1)]
        
        self.assertTrue(player.joker_in_tiles())

    def test_joker_not_in_tiles(self):
        bag_tiles=BagTiles()
        player= Player(bag_tiles)
        player.tiles = [Tile('A', 1), Tile('B', 1), Tile('D', 1)]

        self.assertFalse(player.joker_in_tiles())

    def test_convert_joker_with_joker(self):
        bag_tiles=BagTiles()
        player= Player(bag_tiles)
        player.tiles = [Tile('A', 1), Tile('*', 0), Tile('C', 3)]
        letter_to_convert = 'B'
        player.convert_joker(letter_to_convert)   
        self.assertEqual(player.tiles[1].letter, letter_to_convert.upper())
        self.assertEqual(player.tiles[1].value, 0)

    def test_convert_joker_without_joker(self):
        bag_tiles=BagTiles()
        player= Player(bag_tiles)
        player.tiles = [Tile('A', 1), Tile('C', 3)]
        letter_to_convert = 'B'
        with self.assertRaises (NoJoker):
            player.convert_joker(letter_to_convert)   


if __name__ == '__main__':
    unittest.main()