import unittest
from src.puzzle_game import PuzzleGame
from unittest.mock import patch, Mock
from src.invalid_position_exception import InvalidPositionException


class TestPuzzleGame(unittest.TestCase):

    def test_1_2_3_4(self):
        game = PuzzleGame(2)
        line = 2
        column = 2
        tile = game.get_tile(line, column)
        self.assertEqual(tile, " ")

    def test_1_2_6(self):
        game = PuzzleGame(2)
        line = 0
        column = 0
        with self.assertRaises(Exception):
            game.get_tile(line, column)

# Com mock

    @patch('src.puzzle_game.PuzzleGame.get_tile')
    def test_1_2_3_4_mock(self, mock_game_get_tile):
        game = PuzzleGame(2)
        line = 2
        column = 2
        mock_game_get_tile.return_value = " "
        self.assertEqual(" ", game.get_tile(line, column))

    @patch('src.puzzle_game.PuzzleGame.get_tile')
    def test_1_2_6_mock(self, mock_game_get_tile):
        game = PuzzleGame(2)
        line = 0
        column = 0
        mock_game_get_tile.side_effect = Mock(side_effect=InvalidPositionException())
        with self.assertRaises(Exception):
            game.get_tile(line, column)


if __name__ == '__test_mock_pt1__':
    unittest.main()
