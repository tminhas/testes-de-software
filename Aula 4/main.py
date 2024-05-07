import unittest
from src.puzzle_game import PuzzleGame

from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32, TestingShufflerPuzzleGame2x2To12X3

class TestPuzzleGame(unittest.TestCase):
    
    def setUp(self):
        self.game = PuzzleGame(2)
        self.shuffler12X3 = TestingShufflerPuzzleGame2x2To12X3()
        self.shuffler1X32 = TestingShufflerPuzzleGame2x2To1X32()

    def test_1_2T_3T_4(self):
        self.shuffler12X3.shuffle(self.game)
        initial_line = self.game.line_of_empty_position
        initial_column = self.game.column_of_empty_position
        board = self.game.board
        entry = "DOWN"
        if entry == "DOWN":
            if board.is_in_the_bottom_border(initial_line, initial_column):
                success = self.game.move_empty_tile(entry)
                self.assertFalse(success)
                self.assertEqual(self.game.line_of_empty_position, initial_line)
                self.assertEqual(self.game.column_of_empty_position, initial_column)
                return False
            
    def test_1_2T_3F_5_6(self):
        self.shuffler1X32.shuffle(self.game)
        initial_line = self.game.line_of_empty_position
        initial_column = self.game.column_of_empty_position
        board = self.game.board
        entry = "DOWN"
        if entry == "DOWN":
            if not board.is_in_the_bottom_border(initial_line, initial_column):
                success = self.game.move_empty_tile(entry)
                self.assertTrue(success)
                self.assertEqual(self.game.line_of_empty_position, initial_line + 1)
                self.assertEqual(self.game.column_of_empty_position, initial_column)
                return True


    def test_1_2F_7T_8_9(self):
        self.shuffler1X32.shuffle(self.game)
        initial_line = self.game.line_of_empty_position
        initial_column = self.game.column_of_empty_position
        board = self.game.board
        entry = "UP"
        if entry != "DOWN" and entry == "UP" :
            if board.is_in_the_superior_border(initial_line, initial_column):
                success = self.game.move_empty_tile(entry)
                self.assertFalse(success)
                self.assertEqual(self.game.line_of_empty_position, initial_line)
                self.assertEqual(self.game.column_of_empty_position, initial_column)
                return False
            

    def test_1_2F_7T_8F_10_11(self):
        self.shuffler12X3.shuffle(self.game)
        initial_line = self.game.line_of_empty_position
        initial_column = self.game.column_of_empty_position
        board = self.game.board
        entry = "UP"
        if entry != "DOWN" and entry == "UP":
            if not board.is_in_the_superior_border(initial_line, initial_column):
                success = self.game.move_empty_tile(entry)
                self.assertTrue(success)
                self.assertEqual(self.game.line_of_empty_position, initial_line - 1)
                self.assertEqual(self.game.column_of_empty_position, initial_column)
                return True
            
    def test_1_2F_7F_12T_13T_14(self):
        self.shuffler1X32.shuffle(self.game)
        initial_line = self.game.line_of_empty_position
        initial_column = self.game.column_of_empty_position
        board = self.game.board
        entry = "RIGHT"
        if entry != "DOWN" and entry != "UP" and entry == "RIGHT":
            if board.is_in_the_right_border(initial_line, initial_column):
                success = self.game.move_empty_tile(entry)
                self.assertFalse(success)
                self.assertEqual(self.game.line_of_empty_position, initial_line)
                self.assertEqual(self.game.column_of_empty_position, initial_column)
                return False
            

    def test_1_2F_7F_12T_13F_15_16(self):
        self.shuffler12X3.shuffle(self.game)
        initial_line = self.game.line_of_empty_position
        initial_column = self.game.column_of_empty_position
        board = self.game.board
        entry = "RIGHT"
        if entry != "DOWN" and entry != "UP" and entry == "RIGHT":
            if not board.is_in_the_right_border(initial_line, initial_column):
                success = self.game.move_empty_tile(entry)
                self.assertTrue(success)
                self.assertEqual(self.game.line_of_empty_position, initial_line)
                self.assertEqual(self.game.column_of_empty_position, initial_column + 1)
                return True
            
    def test_1_2F_7F_12F_17T_18T_19(self):
        self.shuffler12X3.shuffle(self.game)
        initial_line = self.game.line_of_empty_position
        initial_column = self.game.column_of_empty_position
        board = self.game.board
        entry = "LEFT"
        if entry != "DOWN" and entry != "UP" and entry != "RIGHT" and entry == "LEFT":
            if board.is_in_the_left_border(initial_line, initial_column):
                success = self.game.move_empty_tile(entry)
                self.assertFalse(success)
                self.assertEqual(self.game.line_of_empty_position, initial_line)
                self.assertEqual(self.game.column_of_empty_position, initial_column)
                return False
            

    def test_1_2F_7F_12T_17T_18F_20_21(self):
        self.shuffler1X32.shuffle(self.game)
        initial_line = self.game.line_of_empty_position
        initial_column = self.game.column_of_empty_position
        board = self.game.board
        entry = "LEFT"
        if entry != "DOWN" and entry != "UP" and entry != "RIGHT" and entry == "LEFT":
            if not board.is_in_the_left_border(initial_line, initial_column):
                success = self.game.move_empty_tile(entry)
                self.assertTrue(success)
                self.assertEqual(self.game.line_of_empty_position, initial_line)
                self.assertEqual(self.game.column_of_empty_position, initial_column - 1)
                return True

    def test_1_2F_7F_12T_17F_22(self):
        self.shuffler1X32.shuffle(self.game)
        entry = ""
        if entry != "DOWN" and entry != "UP" and entry != "RIGHT" and entry != "LEFT":
            return None
            
if __name__ == '__main__':
    unittest.main()