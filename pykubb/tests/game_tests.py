# pylint: disable=C0301,W0622

import unittest
if __name__ == "__main__" and __package__ is None:
    __package__ = "pykubb.tests"
from pykubb.game import Game


class TestGame(unittest.TestCase):
    """Run some tests."""

    def test_game_init(self):
        m = Game()


if __name__ == '__main__':
    unittest.main()