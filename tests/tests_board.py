import unittest
from game.board import Board, SoloVoHParaLaOrientacion
from game.tiles import Tile


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
    



if __name__ == '__main__':
    unittest.main()