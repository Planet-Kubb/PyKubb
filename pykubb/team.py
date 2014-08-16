"""
Planet Kubb Analyzer

This module allows you to import the notation for a match
from a YAML file using Planet Kubb structure and analuze the
aftivity in the games and match. Optionally this module can
augment the original YAML file with calculations and
can generate a Markdown formatted file for each match.
"""
# pylint: disable=C0301,W0622,C0103

import pprint
from pykubb.player import Player


class Team(object):
    """Define a Kubb team."""

    token = None
    win = None
    players = None

    baseline_count = None
    field_count = None
    kubbs_in_hand = None
    throw_count = None
    hit_count = None
    adv_throw_count = None
    adv_hit_count = None
    penalty_count = None
    rethrow_count = None
    inkast_count = None

    history = None

    def __init__(self, team_token = None):
        """Initialize the team."""
        self.token = team_token
        self.win = False

        self.players = {}

        self.baseline_count = 5
        self.field_count = 0
        self.kubbs_in_hand = 0
        self.throw_count = 0
        self.hit_count = 0
        self.adv_throw_count = 0
        self.adv_hit_count = 0
        self.penalty_count = 0
        self.rethrow_count = 0
        self.inkast_count = 0

        self.history = []

    def add_player(self, player_token):
        """Add a player to the team."""
        self.players[player_token] = Player(player_token)
        
    def check_player(self, player_token):
        """Check if a player exists."""
        if player_token not in self.players:
            self.add_player(player_token)
    
    def get_player(self, player_token):
        """Get a player back, creating it if needed."""
        self.check_player(player_token)
        return self.players[player_token]

    def throw(self, batons = 1, player_token = None):
        """The team throws a baton."""
        self.throw_count += batons
        if player_token is not None:
            self.get_player(player_token).throw()

    def miss(self, batons = 1, player_token = None):
        """Baton misses."""
        self.throw(batons, player_token)

    def field_hit(self, kubbs = 1, player_token = None):
        """Field kubb is hit."""
        self.throw(1, player_token)
        self.field_count -= kubbs
        return self.field_count
    
    def lost_base(self, kubbs = 1):
        """Lost a baseline."""
        self.baseline_count -= kubbs
        self.kubbs_in_hand += kubbs

    def hit_base(self, kubbs = 1, player_token = None):
        """Hit opponents baseline."""
        self.throw(1, player_token)
        self.hit_count += 1
        
    def inkast(self, kubbs = 1, player_token = None):
        """Inkastare drills!"""
        self.field_count += kubbs
        self.kubbs_in_hand -= kubbs
        self.inkast_count += kubbs
        if player_token is not None:
            self.get_player(player_token).inkast(kubbs)
    
    def rethrow(self, kubbs = 1, player_token = None):
        """Inkastare rethrows"""
        self.inkast_count += kubbs
        if player_token is not None:
            self.get_player(player_token).rethrow(kubbs)

    def penalty(self, kubbs = 1, player_token = None):
        """Ouch, penalty!"""
        self.penalty_count += kubbs
        if player_token is not None:
            self.get_player(player_token).penalty(kubbs)

    def king(self, player_token = None):
        """King hit! Win!"""
        self.throw(1, player_token)
        self.win = True
    
    def lost(self):
        """Lose!"""
        self.win = False
    
    def won(self):
        """Win!"""
        self.win = True

    def finalize(self):
        """Finalize the game."""
        # for team in ['a', 'b']:
        #     eff_sum = 0
        #     eff_count = 0
        #     for eff_each in self.game[team]['eff1_arr']:
        #         eff_sum += eff_each
        #         eff_count += 1
        #     self.game[team]['eff1'] = float(eff_sum) / float(eff_count)
        pass

    def print_stats(self):
        """Show stats for the team!"""
        print "Stats for team %s:" % self.token
        if self.win:
            print "  WINNER!"
        print "  Throw count: %d" % self.throw_count
        print "  Hit count: %d (%f%%)" % (self.hit_count, (self.hit_count/self.throw_count) * 100)
        print "  Inkast: %d %d %d" % (self.inkast_count, self.rethrow_count, self.penalty_count)
        print "  Kubbs in hand: %d" % (self.kubbs_in_hand)

        for player in self.players:
            self.players[player].print_stats()

