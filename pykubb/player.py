"""
Define player class.

"""

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
        for stat in ['throws', 'hit', 'adv_throws', 'adv_hits', 'penalty', 'rethrow', 'inkast'] :
            self.stats[stat] = 0

    def add_team(self, team):
        """Add a team reference for the player."""
        self.team = team

    def throw(self, batons = 1, hit = False, adv = False):
        """Player throws a baton."""
        self.stats['throws'] += batons
        if hit:
            self.stats['hit'] += batons
        if adv:
            self.stats['adv_throws'] += batons

    def inkast(self, kubbs = 1):
        """Player throws a kubb."""
        self.stats['inkast'] += kubbs

    def print_stats(self):
        """Print stats for the player."""
        print "Stats for player %s" % self.token
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.stats)


