"""
Define the game class.

"""
# pylint: disable=C0301,W0622,C0103

import re
from pykubb.team import Team


class Game(object):
    """Kubb game."""
    
    teams = None
    turn_count = 0
    throwing = 'a'
    defending = 'b'
    throw_count = 0

    def __init__(self):
        """Initialize the game."""
        self.teams = {}
        self.teams['a'] = Team('a')
        self.teams['b'] = Team('b')

    def handle_turn(self, turn):
        """Handle each action in a turn."""
        for action in turn:
            self.handle_action(action)

    def pop_action(self, action):
        """Pull an action off to work on."""
        raction = re.match(
            r'(?P<modifier>\d?)(?P<action>[irpqbf\-=kx])+',
            action)
        if raction is not None:
            mod = raction.group('modifier')
            if mod == '':
                mod = 1
            else:
                mod = int(mod)
            act = raction.group('action')
            new_act = action.replace(raction.group(0), '', 1)
            return mod, act, new_act
        else:
            raise Exception(
                "Failed to parse %s on throw %d." % (
                    action,
                    self.throw_count
                )
            )

    def handle_action(self, raw_action):
        """Handle an action in PK notation"""
        # first unpack the action
        if ':' in raw_action:
            (player, action) = raw_action.split(':')
        else:
            player = None

        while action is not '':
            (mod, action, rem_action) = self.pop_action(action)

            if action == 'b':
                self.teams[self.defending].lost_base(mod)

            if action == 'f':
                self.teams[self.throwing].field_hit(mod, player)

            if action == 'i':
                self.teams[self.throwing].inkast(mod, player)

            if action == 'p':
                self.teams[self.throwing].penalty(mod, player)

            if action == 'k':
                self.teams[self.throwing].king(player)
                self.teams[self.defending].lost()

            if action == 'r':
                self.teams[self.throwing].rethrow(mod, player)

            action = rem_action

    def switch_teams(self):
        """Switch teams!"""
        if self.throwing == 'a':
            self.throwing = 'b'
            self.defending = 'a'
        else:
            self.throwing = 'a'
            self.defending = 'b'

    def finalize(self):
        """Finalize the game by telling each team to finalize."""
        for team in ['a', 'b']:
            self.teams[team].finalize()

    def run(self, plays):
        """Process the array of turns for a game."""
        for turn in plays:
            self.turn_count += 1
            self.handle_turn(turn)
            self.switch_teams()
        self.finalize()

    def print_stats(self):
        """Print stats for the game."""
        self.teams['a'].print_stats()
        self.teams['b'].print_stats()

