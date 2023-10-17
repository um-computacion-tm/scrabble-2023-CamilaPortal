import unittest
from game.cell import Cell
from game.tiles import Tile


class TestCell(unittest.TestCase):

    def test_init(self):
        cell= Cell(multiplier = 2, multiplier_type= 'letter')
        self.assertEqual(cell.multiplier, 2)
        self.assertEqual(cell.multiplier_type, 'letter')
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(), 0
        )

    def test_add_letter(self):
        cell= Cell(multiplier = 1, multiplier_type= '')
        letter= Tile("P", 3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)
    
    def test_cell_value(self):
        cell= Cell(multiplier = 2, multiplier_type= 'letter')
        letter= Tile("P", 3)
        cell.add_letter(letter)

        self.assertEqual(
            cell.calculate_value(), 6
            )
    
    def test_cell_multiplier_word(self):
        cell= Cell(multiplier = 2, multiplier_type= 'word')
        letter= Tile("P", 3)
        cell.add_letter(letter)

        self.assertEqual(
            cell.calculate_value(), 3
        )

    def test_repr_with_letter(self):
        tile = Tile('A', 1)
        cell = Cell(letter=tile)
        self.assertEqual(repr(cell), repr(tile))

    def test_repr_with_multiplier(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        self.assertEqual(repr(cell), 'Wx2')

    def test_repr_with_blank_cell(self):
        cell = Cell()
        self.assertEqual(repr(cell), '   ')



if __name__ == '__main__':
    unittest.main()