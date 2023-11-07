import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame, InvalidWord, InvalidPlaceWordException
from game.board import Board
from game.player import Player
from game.cell import Cell
from game.tiles import Tile, BagTiles

class TestScrabbleGame(unittest.TestCase):

    def test_init(self):
        scrabble_game= ScrabbleGame(3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players), 3
        )
    
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

    # @patch('game.scrabble.ScrabbleGame.validate_word', return_value=True)
    # def test_validate_all(self, mock_validate_word):
    #     scrabble_game = ScrabbleGame(players_count=3)
    #     scrabble_game.current_player = 0
    #     scrabble_game.players[0].tiles = [
    #         Tile('P', 1),
    #         Tile('A', 1),
    #         Tile('L', 1),
    #         Tile('A', 1),
    #         Tile('A', 1),
    #         Tile('A', 1),
    #         Tile('A', 1)
    #     ]
    #     result = scrabble_game.validate_word('PALA', (7, 7), 'H')
    #     self.assertEqual(result, True)

    def test_invalid_word_not_in_dict(self):
        scrabble_game = ScrabbleGame(3)
        with self.assertRaises(InvalidWord):
            scrabble_game.validate_word("ASD", (7, 7), "H")
    
    def test_invalid_word_not_inside_board(self):
        scrabble_game = ScrabbleGame(3)
        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word("PALABRA", (10, 10), "H")
    
    # @patch('game.scrabble.ScrabbleGame.validate_word', return_value=InvalidWord)
    # def test_invalid_word_has_not_letters(self, mock_validate_word):
    #     scrabble_game = ScrabbleGame(players_count=3)
    #     scrabble_game.current_player = scrabble_game.players[0]
    #     scrabble_game.players[0].tiles = [
    #         Tile('P', 1),
    #         Tile('A', 1),
    #         Tile('L', 1),
    #         Tile('A', 1),
    #         Tile('B', 1),
    #         Tile('A', 1),
    #         Tile('A', 1)
    #         ]
    #     mock_validate_word.side_effect = InvalidWord("No tienes las letras para formar esta palabra")
    #     with self.assertRaises(InvalidWord):
    #         scrabble_game.validate_word("HOLA", (7, 7), "H")

    def test_invalid_word_cannot_place(self):
        scrabble_game = ScrabbleGame(3)
        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word("PALABRA", (0, 0), "H")


    @patch('game.scrabble.ScrabbleGame.validate_word')
    def test_valid_word_placement(self, mock_play):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 0
        scrabble_game.players[0].tiles = [
            Tile('H', 4),
            Tile('A', 1),
            Tile('L', 1),
            Tile('A', 1),
            Tile('B', 3),
            Tile('O', 1),
            Tile('A', 1)
            ]
        word = "HOLA"
        location = (7, 7)
        orientation = "H"
        initial_score_player1 = scrabble_game.players[0].score
        scrabble_game.play(word, location, orientation)
        final_score_player1 = scrabble_game.players[0].score
        final_score_player2 = scrabble_game.players[1].score
        final_score_player3 = scrabble_game.players[2].score

        self.assertEqual(initial_score_player1, 0)
        self.assertEqual(final_score_player1, 7)

        self.assertEqual(final_score_player2, 0)
        self.assertEqual(final_score_player3, 0)

    @patch('game.scrabble.ScrabbleGame.validate_word', return_value=6)
    def test_play_horizontal(self, mock_validate_word):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 0
        scrabble_game.players[0].tiles = [
            Tile('P', 3),
            Tile('A', 1),
            Tile('L', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1)
        ]
        scrabble_game.play('PALA', (7, 7), 'H')
        self.assertEqual(scrabble_game.players[0].score, 6)
        self.assertEqual(scrabble_game.board.grid[7][7].letter.letter, 'P')

    @patch('game.scrabble.ScrabbleGame.validate_word', return_value=4)
    def test_play_vertical(self, mock_validate_word):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 0
        scrabble_game.players[0].tiles = [
            Tile('P', 3),
            Tile('A', 1),
            Tile('L', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1)
        ]
        scrabble_game.play('PALA', (7, 7), 'V')
        self.assertEqual(scrabble_game.players[0].score, 6)

    # def test_deactivate_cells_after_play(self):
    #     scrabble_game = ScrabbleGame(2)
    #     scrabble_game.play("CREMA", (7, 7), 'H')

    #     self.assertEqual(scrabble_game.players[0].score, 10)

    #     scrabble_game.play("S", (7, 12), 'H')
    #     self.assertEqual(scrabble_game.players[1].score, 8)





if __name__ == '__main__':
    unittest.main()