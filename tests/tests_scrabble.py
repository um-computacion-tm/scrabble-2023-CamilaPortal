import unittest
from unittest.mock import patch, PropertyMock
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
    @patch('game.tiles.BagTiles.take', return_value=[
        Tile('P', 1),
        Tile('A', 1),
        Tile('L', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1)
    ])
    def test_next_turn_when_game_is_starting(self, mock_take_tiles):
        scrabble_game= ScrabbleGame(3)
        scrabble_game.next_turn()

        self.assertEqual(scrabble_game.current_player, 1)


    def test_next_turn_when_game_is_not_the_first(self):
        scrabble_game= ScrabbleGame(3)
        scrabble_game.current_player = 1

        scrabble_game.next_turn()
        assert scrabble_game.current_player == 2

    @patch('game.tiles.BagTiles.take', return_value=[
        Tile('P', 1),
        Tile('A', 1),
        Tile('L', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1)
    ])
    def test_next_turn_when_player_is_last(self, mock_take_tiles):
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

    @patch('game.tiles.BagTiles.take', return_value=[
        Tile('P', 1),
        Tile('A', 1),
        Tile('L', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1)
    ])
    def test_validate_all(self, mock_take_tiles):
        # Crear un objeto de juego de Scrabble con 3 jugadores
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 0
 
        result = scrabble_game.validate_word('PALA', (7, 7), 'H')
        
        self.assertEqual(result, None)

    @patch('game.tiles.BagTiles.take', return_value=[
        Tile('P', 1),
        Tile('A', 1),
        Tile('L', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1)
    ])
    def test_play(self, mock_take_tiles):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 0
        rack = [Tile('P', 1),
        Tile('A', 1),
        Tile('L', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1)]
 
        result = scrabble_game.play('PALA', (7, 7), 'H', rack )
        
        self.assertEqual(result, None)


    
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


    @patch('game.tiles.BagTiles.take', return_value=[
        Tile('P', 1),
        Tile('A', 1),
        Tile('L', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1)
    ])
    def test_not_get_joker_index(self, mock_take_tiles):
        game = ScrabbleGame(2)
        game.next_turn()

        with self.assertRaises(NoJoker):
            game.get_joker_index()

    @patch('game.tiles.BagTiles.take', return_value=[
        Tile('P', 1),
        Tile('A', 1),
        Tile('L', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1),
        Tile('A', 1)
    ])
    def test_get_player_tiles(self, mock_take_tiles):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 0
        game = ScrabbleGame(3)
        rack = ['P', 'A', 'L', 'A', 'A', 'A', 'A']
        player_tiles = [tile.letter for tile in game.get_player_tiles()]
        self.assertEqual(player_tiles, rack)

    @patch('game.scrabble.ScrabbleGame.get_current_player')
    def test_convert_joker_to_letter(self, mock_get_current_player):
        # Configurar el jugador actual con una ficha comodín
        joker_tile = Tile('*', 0)  # Ficha comodín con letra '?'
        player_with_joker = Player()
        player_with_joker.tiles = [joker_tile]
        
        # Configurar el método get_current_player() para devolver el jugador con el joker
        mock_get_current_player.return_value = player_with_joker
        
        # Crear una instancia de ScrabbleGame y llamar al método convert_joker_to_letter
        scrabble_game = ScrabbleGame(players_count=3)
        letter_to_convert = 'A'  # Letra a la que se debe convertir el joker
        scrabble_game.convert_joker_to_letter(letter_to_convert)
        
        # Verificar que el joker se haya convertido correctamente a la letra especificada
        converted_tile = player_with_joker.tiles[0]
        self.assertEqual(converted_tile.letter, letter_to_convert)

        


if __name__ == '__main__':
    unittest.main()