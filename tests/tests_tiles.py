import unittest
from game.tiles import Tile, BagTiles, NoHayFichas, ImposibleCambiarMasDe7, BolsaLlena, NoEsUnJoker
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile= Tile("A", 1)
        self.assertEqual(tile.letter,"A")
        self.assertEqual(tile.value, 1)
    
    def test_joker(self):
        tile = Tile("*", 0)
        tile.joker('Y')
        self.assertEqual(tile.letter, "Y")
        self.assertEqual(tile.value, 0)
    
    def test_joker2(self):
        tile = Tile("*", 0)
        tile.joker('A')
        self.assertEqual(tile.letter, "A")
        self.assertEqual(tile.value, 0)

    def test_no_joker(self):
        tile = Tile("O", 1)

        with self.assertRaises(NoEsUnJoker):
            tile.joker('A')
        
        self.assertEqual(tile.letter, "O")
        self.assertEqual(tile.value, 1)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag=BagTiles()
        self.assertEqual(
            len(bag.tiles),100 
        )
        self.assertEqual(
            patch_shuffle.call_count, 1
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0], bag.tiles
        )
    
    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),98
        )
        self.assertEqual(
            len(tiles),2
        )
    
    def test_no_hay_fichas(self):
        bag = BagTiles()
        bag.take(100)

        with self.assertRaises(NoHayFichas):
            bag.take(5)
        self.assertEqual(
            len(bag.tiles), 0
            )
    
    def test_put(self):
        bag= BagTiles()
        bag.take(2)
        put_tiles = [Tile("Z", 10), Tile("Y", 4)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles), 100
        )
    
    def test_imposible_intercambiar_mas_de_7(self):
        bag = BagTiles()
        bag.take(7)
        
        with self.assertRaises(ImposibleCambiarMasDe7):
            put_tiles = [Tile("Z", 10), Tile("Y", 4), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1)]
            bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles), 93
        )
    
    def test_bolsa_llena(self):
        bag = BagTiles()

        with self.assertRaises(BolsaLlena):
            put_tiles = [Tile("Z", 10)]
            bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles), 100
        )


if __name__ == '__main__':
    unittest.main()
