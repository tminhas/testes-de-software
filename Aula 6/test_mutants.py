import unittest
from src.puzzle_game import PuzzleGame
from src.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32, TestingShufflerPuzzleGame2x2To12X3


class TestPuzzleGame(unittest.TestCase):

    def setUp(self):
        self.game = PuzzleGame(2)
        self.shuffler12X3 = TestingShufflerPuzzleGame2x2To12X3()
        self.shuffler1X32 = TestingShufflerPuzzleGame2x2To1X32()

    def test_mutant_104(self):
        line = 3
        column = 2
        with self.assertRaises(Exception):
            print("1-2-6")
            self.game.get_tile(line, column)

    def test_mutant_101(self):
        line = 2
        column = 0
        with self.assertRaises(Exception):
            print("1-2-6")
            self.game.get_tile(line, column)

    def test_mutant_98(self):
        line = 0
        column = 2
        with self.assertRaises(Exception):
            print("1-2-6")
            self.game.get_tile(line, column)


    def test_mutant_no_number1(self):
        line = 1
        column = 1
        tile = self.game.get_tile(line, column)
        success = self.game.move_tile(tile)
        self.assertFalse(success)


    def test_mutant_no_number2(self):
        line = 1
        column = 1
        success = self.game.move_tile_from_a_position_to_the_empty_position(line, column)
        self.assertFalse(success)

if __name__ == '__test_mutants__':
    unittest.main()
