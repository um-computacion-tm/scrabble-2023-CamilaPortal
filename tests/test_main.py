import unittest
from unittest.mock import patch
from game.main import Main
from game.scrabble import ScrabbleGame
from game.cell import Cell
from game.board import Board
import io
import sys

class TestCLI(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        main= Main()
        self.assertEqual(
            main.get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        main= Main()
        self.assertEqual(
            main.get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '2'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        main= Main()
        self.assertEqual(
            main.get_player_count(),
            2,
        )

    @patch('builtins.input', side_effect=[2, 3])
    def test_get_location_valid_input(self, mock_input):
        instance = Main()
        result = instance.get_location()
        self.assertEqual(result, (2, 3))

    @patch('builtins.input', side_effect=['a', 'b', 2, 3])
    def test_get_location_invalid_then_valid_input(self, mock_input):
        instance = Main()
        result = instance.get_location()
        self.assertEqual(result, (2, 3))

    @patch('builtins.input', side_effect=['H'])
    def test_get_orientation_horizontal_input(self, mock_input):
        instance = Main()
        result = instance.get_orientation()
        self.assertEqual(result, 'H')

    @patch('builtins.input', side_effect=['V'])
    def test_get_orientation_vertical_input(self, mock_input):
        instance = Main()
        result = instance.get_orientation()
        self.assertEqual(result, 'V')

    @patch('builtins.input', side_effect=['X', 'H'])
    def test_get_orientation_invalid_then_valid_input(self, mock_input):
        instance = Main()
        result = instance.get_orientation()
        self.assertEqual(result, 'H')

    def test_get_word_valid_input(self):
        main = Main()
        with unittest.mock.patch('builtins.input', side_effect=["word"]):
            word = main.get_word()
        self.assertEqual(word, "WORD")

    
    @patch('builtins.input', side_effect=["*", "a"])
    def test_get_word(self, mock_input):
        main = Main()
        word = main.get_word()
        self.assertEqual(word, "A")

    @patch('builtins.input', side_effect=["MESA"])
    def test_get_word2(self, mock_input):
        main = Main()
        word = main.get_word()
        self.assertEqual(word, "MESA")


    @patch.object(ScrabbleGame, 'next_turn')
    def test_pass_turn(self, mock_next_turn):
        main_instance = Main()
        game_mock = ScrabbleGame(2)
        main_instance.pass_turn(game_mock)
        mock_next_turn.assert_called_once()

    # @patch('builtins.input', side_effect=['A'])
    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_joker_with_valid_input(self, mock_stdout, mock_input):
    #     main_instance = Main()
    #     game_mock = Mock()
    #     game_mock.get_joker_index.return_value = 1
    #     main_instance.joker(game_mock)
    #     output = mock_stdout.getvalue().strip()
    #     game_mock.convert_joker_to_letter.assert_called_once_with('A')
    #     # Verifica que la salida estándar incluya el mensaje esperado
    #     self.assertIn('Ingrese la letra por la que desea cambiar el comodin:', output)





if __name__ == '__main__':
    unittest.main()