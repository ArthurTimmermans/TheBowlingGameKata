import unittest
import Bowling

class TestBowling(unittest.TestCase):

    def test_game_start(self):
        game = Bowling.game()
        self.assertEqual((0,0,0,1,1), game.gameInfo())

    def test_game_adds_score(self):
        game = Bowling.game()
        game.roll(2)
        self.assertEqual((0,0,2,1,2), game.gameInfo())
        game.roll(2)
        self.assertEqual((0,0,4,1,3), game.gameInfo())
        game.roll(2)
        self.assertEqual((4,0,2,2,2), game.gameInfo())
        game.roll(3)
        self.assertEqual((4,0,5,2,3), game.gameInfo())
        game.roll(2)
        self.assertEqual((9,0,2,3,2), game.gameInfo())

    def test_strike_score(self):
        game = Bowling.game()
        game.roll(10)
        self.assertEqual((0,10,0,1,3), game.gameInfo())
        game.roll(2)
        self.assertEqual((10,0,2,2,2), game.gameInfo())