import unittest
from game.board import Board, SoloVoHParaLaOrientacion, NoValid, WordOutOfBoard, NotEnoughLetters
from game.tiles import Tile, BagTiles
from game.cell import Cell
from game.player import Player


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
    
    def test_initial_board_setup2(self):
        board = Board()
        self.assertEqual(board.grid[1][1].multiplier_type, 'word')
        self.assertEqual(board.grid[1][1].multiplier, 2)

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

        self.assertEqual(board.validate_word_inside_board(word, location, orientation), False)
        
    
    def test_word_out_of_board_V(self):
        board = Board()
        word = "Facultad"
        location = (9, 3)
        orientation = "V"

        self.assertEqual(board.validate_word_inside_board(word, location, orientation), False)

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
        location = (8, 6)
        orientation = "H"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        self.assertEqual(word_is_valid, True)

    def test_place_word_not_empty_board_horizontal_wrong(self):
        board = Board()
        board.grid[7] [7].add_letter(Tile('C', 1))
        board.grid[8] [7].add_letter(Tile('A', 1))
        board.grid[9] [7].add_letter(Tile('S', 1))
        board.grid[10] [7].add_letter(Tile('A', 1))
        word = "FACULTAD"
        location = (9, 6)
        orientation = "H"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        self.assertEqual(word_is_valid, False)
    
    def test_place_word_not_empty_board_horizontal_out_of_board(self):
        board = Board()
        board.grid[7] [7].add_letter(Tile('C', 1))
        board.grid[8] [7].add_letter(Tile('A', 1))
        board.grid[9] [7].add_letter(Tile('S', 1))
        board.grid[10] [7].add_letter(Tile('A', 1))
        word = "FACULTADES"
        location = (8, 6)
        orientation = "H"

        with self.assertRaises(WordOutOfBoard):
            board.validate_word_place_board(word, location, orientation)

    def test_place_word_not_empty_board_vertical_fine(self):
        board = Board()
        board.grid[7] [7].add_letter(Tile('C', 1))
        board.grid[7] [8].add_letter(Tile('A', 1))
        board.grid[7] [9].add_letter(Tile('S', 1))
        board.grid[7] [10].add_letter(Tile('A', 1))
        word = "FACULTAD"
        location = (6, 8)
        orientation = "V"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        self.assertEqual(word_is_valid, True)
    
    def test_place_word_not_empty_board_vertical_wrong(self):
        board = Board()
        board.grid[7] [7].add_letter(Tile('C', 1))
        board.grid[7] [8].add_letter(Tile('A', 1))
        board.grid[7] [9].add_letter(Tile('S', 1))
        board.grid[7] [10].add_letter(Tile('A', 1))
        word = "FACULTAD"
        location = (6, 9)
        orientation = "V"

        word_is_valid = board.validate_word_place_board(word, location, orientation)

        self.assertEqual(word_is_valid, False)

    def test_place_word_not_empty_board_vertical_out_of_board(self):
        board = Board()
        board.grid[7] [7].add_letter(Tile('C', 1))
        board.grid[7] [8].add_letter(Tile('A', 1))
        board.grid[7] [9].add_letter(Tile('S', 1))
        board.grid[7] [10].add_letter(Tile('A', 1))
        word = "FACULTADES"
        location = (6, 8)
        orientation = "V"

        with self.assertRaises(WordOutOfBoard):
            board.validate_word_place_board(word, location, orientation)

    def test_put_word_horizontal_valid(self):
        board=Board()
        word = "hola"
        location = (7, 6)
        orientation = "H"
        board.put_word(word, location, orientation)
        

    def test_put_word_vertical_valid(self):
        board=Board()
        word = "mundo"
        location = (6, 7)
        orientation = "V"
        board.put_word(word, location, orientation)

    def test_put_word_invalid_location(self):
        board=Board()
        word = "hola"
        location = (0, 0)
        orientation = "X"
        with self.assertRaises(SoloVoHParaLaOrientacion):
            board.put_word(word, location, orientation)

    # def test_draw_board(self):
    #     board = Board()
    #     expected_board = (
    #         "     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15\n"
    #         " 1|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         " 2|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         " 3|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         " 4|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         " 5|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         " 6|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         " 7|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         " 8|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         " 9|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         "10|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         "11|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         "12|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         "13|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         "14|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #         "15|  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n"
    #     )
    #     result_board = board.draw_board()
    #     self.assertEqual(result_board, expected_board)

if __name__ == '__main__':
    unittest.main()