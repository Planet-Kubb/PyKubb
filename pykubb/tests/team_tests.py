# pylint: disable=C0301,W0622

import unittest
if __name__ == "__main__" and __package__ is None:
    __package__ = "pykubb.tests"
from pykubb.team import Team


class TestPlayer(unittest.TestCase):
    """Run some tests."""

    def test_team_throw(self):
        t = Team('a')
        t.throw()
        assert t.throw_count == 1


if __name__ == '__main__':
    unittest.main()