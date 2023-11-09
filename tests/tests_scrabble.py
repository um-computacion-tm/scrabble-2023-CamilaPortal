import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame, InvalidWord, InvalidPlaceWordException, NoJoker
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

    # def test_invalid_word_not_in_dict(self):
    #     scrabble_game = ScrabbleGame(3)
    #     with self.assertRaises(InvalidWord):
    #         scrabble_game.validate_in_dict("ASD")
    
    def test_invalid_word_not_inside_board(self):
        scrabble_game = ScrabbleGame(3)
        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word("PALABRA", (10, 10), "H")


    def test_invalid_word_cannot_place(self):
        scrabble_game = ScrabbleGame(3)
        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word("PALABRA", (0, 0), "H")

    def compare_score(self):
        game = ScrabbleGame(3)
        game.players[0].score = 50
        game.players[1].score = 30
        game.players[2].score = 40
        result = game.compare_score()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].score, 50)
    
    def test_compare_score_multiple_winners(self):
        game = ScrabbleGame(3)
        game.players[0].score = 50
        game.players[1].score = 50
        game.players[2].score = 40
        result = game.compare_score()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].score, 50)
        self.assertEqual(result[1].score, 50)

    def test_finish_game_empty_bag(self):
        game = ScrabbleGame(3)
        game.bag_tiles.tiles = []
        result = game.finish_game()
        self.assertTrue(result)

    def test_finish_game_non_empty_bag(self):
        game = ScrabbleGame(3)
        game.bag_tiles.tiles = [Tile('A', 1), Tile('B', 3)]
        result = game.finish_game()
        self.assertFalse(result)

    def test_get_joker_index(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.get_current_player().tiles = [
            Tile(letter='A', value=1),
            Tile(letter='*', value=0),
            Tile(letter='B', value=3)
        ]
        index = game.get_joker_index()
        self.assertEqual(index, 1)

    # def test_play(self):
    #     game=ScrabbleGame(2)
    #     word="asd"
    #     location= (7,7)
    #     orientation="H"

    #     result=game.play(word, location, orientation)

    #     self.assertEqual(result, False)


    # def test_get_joker_index_without_joker(self):
    #     tiles_without_joker = ['A', 'B', 'C', 'D']
    #     player = Player(tiles_without_joker)
    #     # Asegúrate de que se lance la excepción ValueError si el jugador no tiene comodín
    #     with self.assertRaises(ValueError):
    #         player.get_joker_index()

    # def test_get_tiles(self):
    #     game = ScrabbleGame(3)

    #     self.assertEqual(game.get_player_tiles(), ['A', 'B', 'C'])
        


if __name__ == '__main__':
    unittest.main()