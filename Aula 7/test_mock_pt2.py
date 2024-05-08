import unittest
from src.puzzle_game_with_mock import PuzzleGameWithPlayer
from src.shufflers_for_testing_puzzles import (TestingShufflerPuzzleGame2x2To12X3,
                                               TestingShufflerPuzzleGame2x2To1X32)
from unittest.mock import patch, Mock
from src.invalid_position_exception import InvalidPositionException


class TestPuzzleGame(unittest.TestCase):

    def setUp(self):
        self.game = PuzzleGameWithPlayer(2, "Thomas")
        self.shuffler12X3 = TestingShufflerPuzzleGame2x2To12X3()
        self.shuffler1X32 = TestingShufflerPuzzleGame2x2To1X32()

    def test_game_ended(self):
        self.shuffler12X3.shuffle(self.game)
        self.game.move_tile_from_a_position_to_the_empty_position(2, 2)
        self.assertEqual('Saved', self.game.end_of_the_game())

    def test_game_not_ended(self):
        self.shuffler12X3.shuffle(self.game)
        self.game.move_tile_from_a_position_to_the_empty_position(2, 1)
        self.assertEqual('Game not finished', self.game.end_of_the_game())

    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_save_game(self, mock_game_save_game_to_file):
        self.shuffler12X3.shuffle(self.game)
        self.game.move_tile_from_a_position_to_the_empty_position(2, 2)
        mock_game_save_game_to_file.return_value = 'Saved'
        self.assertEqual('Saved', self.game.end_of_the_game())

    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_save_game_2(self, mock_game_save_game_to_file):
        self.shuffler1X32.shuffle(self.game)
        mock_game_save_game_to_file.return_value = 'Saved'
        self.assertEqual('Game not finished', self.game.end_of_the_game())


if __name__ == '__test_mock_pt2__':
    unittest.main()
