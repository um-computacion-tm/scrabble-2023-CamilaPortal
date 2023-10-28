import unittest
from game.scrabble import ScrabbleGame, InvalidWord, InvalidPlaceWordException
from game.board import Board
from game.player import Player

class TestScrabbleGame(unittest.TestCase):

    def test_init(self):
        scrabble_game= ScrabbleGame(3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players), 3
        )

        self.assertIsNotNone(scrabble_game.bag_tiles)
    
    def test_next_turn_when_game_is_starting(self):
        scrabble_game= ScrabbleGame(3)
        scrabble_game.next_turn()

        self.assertEqual(scrabble_game.current_player, 1)


    def test_next_turn_when_game_is_not_the_first(self):
        scrabble_game= ScrabbleGame(3)
        scrabble_game.current_player = 1

        scrabble_game.next_turn()
        assert scrabble_game.current_player == 2

    def test_next_turn_when_player_is_last(self):
        scrabble_game= ScrabbleGame(3)
        scrabble_game.current_player = 3

        scrabble_game.next_turn()
        assert scrabble_game.current_player == 1

    def test_is_playing(self):
        scrabble_game= ScrabbleGame(3)
        self.assertEqual(scrabble_game.is_playing(), True)

    def test_get_current_player(self):
        scrabble_game = ScrabbleGame(3)
        current_player = scrabble_game.get_current_player()
        self.assertIsNotNone(current_player)
        self.assertIsInstance(current_player, Player)

    def test_get_board(self):
        scrabble_game = ScrabbleGame(3)
        board= scrabble_game.get_board()
        self.assertIsNotNone(board)
        self.assertIsInstance(board, Board)

    def test_valid_word(self):
        scrabble_game = ScrabbleGame(3)  
        result = scrabble_game.validate_word("PALABRA", (7, 7), "H")
        self.assertEqual(result, None)

    def test_invalid_word_not_in_dict(self):
        scrabble_game = ScrabbleGame(3)
        with self.assertRaises(InvalidWord):
            scrabble_game.validate_word("ASD", (7, 7), "H")
    
    def test_invalid_word_not_inside_board(self):
        scrabble_game = ScrabbleGame(3)
        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word("PALABRA", (10, 10), "H")

    def test_invalid_word_cannot_place(self):
        scrabble_game = ScrabbleGame(3)
        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word("PALABRA", (0, 0), "H")



if __name__ == '__main__':
    unittest.main()