"""
Define player class.

"""

import pprint
import logging


class Player():
    """Kubb player."""
    
    token = None
    stats = None
    team = None

    def __init__(self, token = None):
        self.token = token
        self.stats = {}
        for stat in ['throws', 'hit', 'adv_throws', 'adv_hits', 'penalty', 'rethrow', 'inkast'] :
            self.stats[stat] = 0

    def add_team(self, team):
        self.__team = team

    def throw(self, batons = 1, hit = False, adv = False):
        self.stats['throws'] += batons
        if hit:
            self.stats['hit'] += batons
        if adv:
            self.stats['adv_throws'] += batons

    def inkast(self, kubbs = 1):
        self.stats['inkast'] += kubbs

    def print_stats(self):
        print "Stats for player %s" % self.token
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.stats)


