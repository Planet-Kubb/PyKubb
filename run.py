#!/usr/bin/python

"""
Planet Kubb Analyzer

This module allows you to import the notation for a match
from a YAML file using Planet Kubb structure and analuze the
aftivity in the games and match. Optionally this module can
augment the original YAML file with calculations and
can generate a Markdown formatted file for each match.
"""

from pykubb.game import Game


# Run
if __name__ == '__main__':
    m = Game()

    plays = [
        ['a:-', 'a:-', 'a:b', 'b:b', 'b:-', 'b:b'],
        ['c:3i', 'c:f', 'c:f', 'c:-', 'd:f', 'd:-', 'd:i'],
        ['a:3i', 'a:2f', 'a:f', 'a:-', 'b:-', 'b:-', 'b:-'],
        ['c:3i', 'c:2f', 'c:-', 'c:f', 'd:-', 'd:b', 'd:b'],
        ['a:5i2rp', 'a:4f', 'a:f', 'a:b-', 'b:-', 'b:b', 'b:k']
    ]
    m.run(plays)
    m.print_stats()

    m = None

