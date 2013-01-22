import unittest

class BowlingGame():
    def __init__(self):
        self.totalScore = 0
    def roll(self, pins):
        self.totalScore += pins
    def score(self):
        return self.totalScore

class BowlingGameTest(unittest.TestCase):
    def test_GutterGame(self):
        game = BowlingGame()
        for i in range(20):
            game.roll(0)
        self.assertEqual(0, game.score())
    
    def test_RollAllOnes(self):
        game = BowlingGame()
        for i in range(20):
            game.roll(1)
        self.assertEqual(20, game.score())

    def test_RollSpare(self):
        game = BowlingGame()
        game.roll(2)
        game.roll(8)
        game.roll(5)
        self.asserEqual(15)

    def test_RollStrike(self):
        None
    
    def test_PerfectGame(self):
        None
