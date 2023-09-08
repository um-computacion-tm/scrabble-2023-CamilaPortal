import unittest
from game.cell import Cell
from game.tiles import Tile

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        cell= Cell()
         
        word = [
            Cell(letter=Tile("C", 1)),
            Cell(letter=Tile("A", 1)),
            Cell(letter=Tile("S", 2)),
            Cell(letter=Tile("A", 1))
        ]

        value = cell.calculate_word_value(cells=word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        cell = Cell()
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A', 1)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        cell=Cell()
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A', 1)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 10)
    
    def test_with_both_multiplier(self):
        cell=Cell()
        word = [
            Cell(letter = Tile("C", 3), multiplier=2, multiplier_type='word'),
            Cell(letter = Tile("A", 1), multiplier=3, multiplier_type='letter'),
            Cell(letter = Tile("S", 1), multiplier=1, multiplier_type=''),
            Cell(letter = Tile("A", 1), multiplier=1, multiplier_type='')
        ]

        value = cell.calculate_word_value(cells=word)

        self.assertEqual(
            value, 16
        )

    def test_with_both_multiplier_cell_not_active(self):
        cell=Cell()
        
        word = [
            Cell(letter = Tile("C", 3), multiplier=2, multiplier_type='word', active=False),
            Cell(letter = Tile("A", 1), multiplier=3, multiplier_type='letter', active=False),
            Cell(letter = Tile("S", 1), multiplier=1, multiplier_type='', active=False),
            Cell(letter = Tile("A", 1), multiplier=1, multiplier_type='', active=False)
        ]

        
        value = cell.calculate_word_value(cells=word)

        self.assertEqual(
            value, 6
        )
    
    

if __name__ == '__main__':
     unittest.main()