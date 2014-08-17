# pylint: disable=C0301,W0622,C0103

import unittest
if __name__ == "__main__" and __package__ is None:
    __package__ = "pykubb.tests"
from pykubb.game import Game


class TestGame(unittest.TestCase):
    """Run some tests."""

    def test_complete_game1(self):
        """Run entire game through engine."""
        m = Game()

        plays = [
            ['a:-', 'a:-', 'a:b', 'b:b', 'b:-', 'b:b'],
            ['c:3i', 'c:f', 'c:f', 'c:-', 'd:f', 'd:-', 'd:-'],
            ['a:3i', 'a:2f', 'a:f', 'a:-', 'b:-', 'b:-', 'b:-'],
            ['c:3i', 'c:2f', 'c:-', 'c:f', 'd:-', 'd:b', 'd:b'],
            ['a:5i2rp', 'a:4f', 'a:f', 'a:b-', 'b:-', 'b:b', 'b:k']
        ]
        m.run(plays)
        m.print_stats()

        # Did the right team win?
        assert m.teams['a'].win == True

        # Did we get 5 turns?
        assert m.turn_count == 5

        # There should have been 30 throws in the game
        assert m.get_throw_count() == 30


if __name__ == '__main__':
    unittest.main()
