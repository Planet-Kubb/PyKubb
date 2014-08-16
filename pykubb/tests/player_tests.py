# pylint: disable=C0301,W0622

import unittest
if __name__ == "__main__" and __package__ is None:
    __package__ = "pykubb.tests"
from pykubb.player import Player


class TestPlayer(unittest.TestCase):
    """Run some tests."""

    def test_player_init(self):
        p = Player('jamie')
        assert p.token == 'jamie'

    def test_player_throw(self):
        p = Player('a')
        p.throw()
        assert p.throw_count == 1


if __name__ == '__main__':
    unittest.main()