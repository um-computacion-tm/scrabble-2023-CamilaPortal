import unittest
from game.cell import Cell, calculate_word_value
from game.tiles import Tile

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
         word = [
            Cell(letter=Tile("C", 1)),
            Cell(letter=Tile("A", 1)),
            Cell(letter=Tile("S", 2)),
            Cell(letter=Tile("A", 1))
        ]
         
         value= calculate_word_value(word)
         self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 10)
    
    def test_with_both_multiplier(self):
        word = [
            Cell(letter = Tile("C", 3), multiplier=2, multiplier_type='word'),
            Cell(letter = Tile("A", 1), multiplier=3, multiplier_type='letter'),
            Cell(letter = Tile("S", 1), multiplier=1, multiplier_type=''),
            Cell(letter = Tile("A", 1), multiplier=1, multiplier_type='')
        ]

        value = calculate_word_value(cells=word)

        self.assertEqual(
            value, 16
        )
    
    

if __name__ == '__main__':
     unittest.main()