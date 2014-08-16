"""
Define player class.

"""
# pylint: disable=C0301,W0622,C0103

import pprint


class Player(object):
    """Kubb player."""
    
    token = None
    stats = None
    team = None

    def __init__(self, token = None):
        """Initializer the player."""
        self.token = token
        self.stats = {}
        for stat in [
            'throws',
            'hit',
            'adv_throws',
            'adv_hits',
            'penalty',
            'rethrow',
            'inkast']:
            self.stats[stat] = 0

    def add_team(self, team):
        """Add a team reference for the player."""
        self.team = team

    def throw(self, batons = 1):
        """Player throws a baton."""
        self.stats['throws'] += batons
        return self.stats['throws']

    def inkast(self, kubbs = 1):
        """Player throws a kubb."""
        self.stats['inkast'] += kubbs
        return self.stats['inkast']

    def rethrow(self, kubbs = 1):
        """Player throws a kubb."""
        self.stats['rethrow'] += kubbs
        return self.stats['rethrow']

    def penalty(self, kubbs = 1):
        """Player throws a kubb."""
        self.stats['penalty'] += kubbs
        return self.stats['penalty']

    def print_stats(self):
        """Print stats for the player."""
        print "Stats for player %s" % self.token
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.stats)


