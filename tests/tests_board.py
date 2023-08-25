import unittest
from game.board import Board


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

if __name__ == '__main__':
    unittest.main()