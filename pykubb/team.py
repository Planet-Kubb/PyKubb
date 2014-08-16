"""
Planet Kubb Analyzer

This module allows you to import the notation for a match
from a YAML file using Planet Kubb structure and analuze the
aftivity in the games and match. Optionally this module can
augment the original YAML file with calculations and
can generate a Markdown formatted file for each match.
"""

import pprint
import logging
from pykubb.player import Player


class Team():
    token = None
    players = None
    stats = None

    def __init__(self, team_token = None):
        self.token = team_token
        self.players = {}
        self.stats = {}
        self.stats['baseline'] = 5
        for stat in ['field', 'kih', 'throws', 'inkast', 'hit', 'adv', 'penalty', 'rethrow']:
            self.stats[stat] = 0

    def add_player(self, player_token):
        self.players[player_token] = Player(player_token)
        
    def check_player(self, player_token):
        if player_token not in self.players:
            self.add_player(player_token)
    
    def get_player(self, player_token):
        self.check_player(player_token)
        return self.players[player_token]

    def throw(self, player_token = None):
        self.stats['throws'] += 1
        if player_token is not None:
            self.get_player(player_token).throw()
    
    def field_hit(self, kubbs = 1, player_token = None):
        self.throw(player_token)
        self.stats['field'] -= kubbs
    
    def lost_base(self, kubbs = 1, player_token = None):
        self.stats['baseline'] -= kubbs
    
    def inkast(self, kubbs = 1, player_token = None):
        self.stats['field'] += kubbs
        self.stats['kih'] -= kubbs
        self.stats['inkast'] += kubbs
        if player_token is not None:
            self.get_player(player_token).inkast(kubbs)
    
    def rethrow(self, kubbs = 1, player_token = None):
        self.stats['inkast'] += kubbs
    
    def penalty(self, kubbs = 1, player_token = None):
        self.stats['penalty'] += kubbs
    
    def king(self, player_token = None):
        self.throw(player_token)
        self.won()
    
    def lost(self):
        self.stats['won'] = False
    
    def won(self):
        self.stats['won'] = True

    def print_stats(self):
        print "Stats for team %s:" % self.token
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.stats)
        
        for player in self.players:
            self.players[player].print_stats()

