import unittest
from game.cell import Cell
from game.tiles import Tile
from game.board import Board

class TestCalculateWordValue(unittest.TestCase):
    def test_empty_cell(self):
        cell = Cell()
        value = cell.calculate_value()
        self.assertEqual(value, 0)

    def test_active_letter_multiplier(self):
        tile = Tile('A', 1)
        cell = Cell(letter=tile, multiplier=2, multiplier_type='letter', active=True)
        value = cell.calculate_value()
        self.assertEqual(value, 2)

    def test_inactive_letter_multiplier(self):
        tile = Tile('B', 3)
        cell = Cell(letter=tile, multiplier=3, multiplier_type='letter', active=False)
        value = cell.calculate_value()
        self.assertEqual(value, 9)

    def test_no_multiplier(self):
        tile = Tile('D', 2)
        cell = Cell(letter=tile, active=True)
        value = cell.calculate_value()
        self.assertEqual(value, 2)

    def test_empty_cell_inactive(self):
        cell = Cell(active=False)
        value = cell.calculate_value()
        self.assertEqual(value, 0)

    def test_with_word_multiplier(self):
        board= Board()
        word = [
            Cell(letter=Tile('C', 3)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 1),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 12)
    
    

if __name__ == '__main__':
     unittest.main()