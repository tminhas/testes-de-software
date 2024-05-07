import unittest
from src.puzzle_game import PuzzleGame


class TestPuzzleGame(unittest.TestCase):

    def setUp(self):
        self.game = PuzzleGame(2)

    def test_1_2_3_5(self):
        line = 1
        column = 1
        tile = self.game.get_tile(line, column)
        self.assertEqual(tile, 1)
        print("1-2-3-5")

    def test_1_2_3_4(self):
        line = 2
        column = 2
        tile = self.game.get_tile(line, column)
        self.assertEqual(tile, " ")
        print("1-2-3-4")

    def test_1_2_6(self):
        line = 0
        column = 0
        with self.assertRaises(Exception):
            print("1-2-6")
            self.game.get_tile(line, column)


if __name__ == '__gfd__':
    unittest.main()
