import unittest
from game.board import Board, SoloVoHParaLaOrientacion
from game.tiles import Tile
from game.cell import Cell


class TestBoard(unittest.TestCase):

    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid), 15
        )

        self.assertEqual(
            len(board.grid[0]), 15
        )

    def test_initial_board_setup(self):
        board = Board()
        self.assertEqual(board.grid[0][0].multiplier_type, 'word')
        self.assertEqual(board.grid[0][0].multiplier, 3)

    def test_word_inside_board_H(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    
    def test_word_inside_board_V(self):
        board = Board()
        word = "Facultad"
        location = (1, 1)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    
    def test_word_out_of_board_H(self):
        board = Board()
        word = "Facultad"
        location = (14, 9)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False
        
    
    def test_word_out_of_board_V(self):
        board = Board()
        word = "Facultad"
        location = (9, 3)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False

    def test_incorrect_orientation(self):
        board = Board()
        word = "Facultad"
        location = (1, 1)
        orientation = "X"

        with self.assertRaises(SoloVoHParaLaOrientacion):
            board.validate_word_inside_board(word, location, orientation)
    
    def test_board_empty(self):
        board = Board()
        assert board.is_empty() == True
    
    def test_board_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 3))
        assert board.is_empty() == False
    
    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        assert word_is_valid == False
    
    def test_place_word_empty_board_orientation_wrong(self):

        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "X"

        with self.assertRaises(SoloVoHParaLaOrientacion):
            board.validate_word_place_board(word, location, orientation)
    
    def test_place_word_empty_board_vertical_fine(self):
        
        board = Board()
        word = "FACULTAD"
        location = (4, 7)
        orientation = "V"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        assert word_is_valid == False

    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7] [7].add_letter(Tile('C', 1))
        board.grid[8] [7].add_letter(Tile('A', 1))
        board.grid[9] [7].add_letter(Tile('S', 1))
        board.grid[10] [7].add_letter(Tile('A', 1))
        word = "FACULTAD"
        location = (10, 6)
        orientation = "H"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        self.assertEqual(word_is_valid, True)

if __name__ == '__main__':
    unittest.main()