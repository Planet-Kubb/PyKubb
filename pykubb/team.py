"""
Planet Kubb Analyzer

This module allows you to import the notation for a match
from a YAML file using Planet Kubb structure and analuze the
aftivity in the games and match. Optionally this module can
augment the original YAML file with calculations and
can generate a Markdown formatted file for each match.
"""

import pprint
from pykubb.player import Player


class Team(object):
    """Define a Kubb team."""

    token = None
    players = None
    stats = None

    def __init__(self, team_token = None):
        """Initialize the team."""
        self.token = team_token
        self.players = {}
        self.stats = {}
        self.stats['baseline'] = 5
        for stat in ['field', 'kih', 'throws', 'inkast', 'hit', 'adv', 'penalty', 'rethrow']:
            self.stats[stat] = 0

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

    def throw(self, player_token = None):
        """The team throws a baton."""
        self.stats['throws'] += 1
        if player_token is not None:
            self.get_player(player_token).throw()
    
    def field_hit(self, kubbs = 1, player_token = None):
        """Field kubb is hit."""
        self.throw(player_token)
        self.stats['field'] -= kubbs
    
    def lost_base(self, kubbs = 1, player_token = None):
        """Lost a baseline."""
        self.stats['baseline'] -= kubbs
    
    def inkast(self, kubbs = 1, player_token = None):
        """Inkastare drills!"""
        self.stats['field'] += kubbs
        self.stats['kih'] -= kubbs
        self.stats['inkast'] += kubbs
        if player_token is not None:
            self.get_player(player_token).inkast(kubbs)
    
    def rethrow(self, kubbs = 1, player_token = None):
        """Inkastare rethrows"""
        self.stats['inkast'] += kubbs
    
    def penalty(self, kubbs = 1, player_token = None):
        """Ouch, penalty!"""
        self.stats['penalty'] += kubbs
    
    def king(self, player_token = None):
        """King hit! Win!"""
        self.throw(player_token)
        self.won()
    
    def lost(self):
        """Lose!"""
        self.stats['won'] = False
    
    def won(self):
        """Win!"""
        self.stats['won'] = True

    def print_stats(self):
        """Show stats for the team!"""
        print "Stats for team %s:" % self.token
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.stats)
        
        for player in self.players:
            self.players[player].print_stats()

