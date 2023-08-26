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

    def test_cell_multiplier_word2(self):
        cell1 = Cell(multiplier=2, multiplier_type='word')
        letter1 = Tile("C", 3)
        cell1.add_letter(letter1)

        cell2 = Cell(multiplier=3, multiplier_type='letter')
        letter2 = Tile("A", 1)
        cell2.add_letter(letter2)

        cell3 = Cell(multiplier=1, multiplier_type='')
        letter3 = Tile("S", 1)
        cell3.add_letter(letter3)

        cell4 = Cell(multiplier=1, multiplier_type='')
        letter4 = Tile("A", 1)
        cell4.add_letter(letter4)

        cells = [cell1, cell2, cell3, cell4]

        result = Cell.calculate_word_value(self, cells)

        self.assertEqual(
            result, 16
        )

if __name__ == '__main__':
    unittest.main()