"""
Define player class.

"""
# pylint: disable=C0301,W0622,C0103


class Player(object):
    """Kubb player."""
    
    token = None

    throw_count = None
    hit_count = None
    miss_count = None
    adv_throw_count = None
    adv_hit_count = None
    penalty_count = None
    rethrow_count = None
    inkast_count = None
    king_miss = None

    history = None

    def __init__(self, token = None):
        """Initializer the player."""
        self.token = token

        self.throw_count = 0
        self.hit_count = 0
        self.miss_count = 0
        self.adv_throw_count = 0
        self.adv_hit_count = 0
        self.penalty_count = 0
        self.rethrow_count = 0
        self.inkast_count = 0
        self.king_miss = 0

        self.history = []

    def throw(self, batons = 1):
        """Player throws a baton."""
        self.throw_count += batons
        return self.throw_count

    def miss(self, batons = 1):
        """Player misses."""
        self.miss_count += batons
        return self.miss_count

    def inkast(self, kubbs = 1):
        """Player throws a kubb."""
        self.inkast_count += kubbs
        return self.inkast_count

    def rethrow(self, kubbs = 1):
        """Player throws a kubb."""
        self.rethrow_count += kubbs
        return self.rethrow_count

    def penalty(self, kubbs = 1):
        """Player throws a kubb."""
        self.penalty_count += kubbs
        return self.penalty_count

    def king_miss(self, batons = 1):
        """Player missed king."""
        self.king_miss += 1
        return self.king_miss

    def print_stats(self):
        """Print stats for the player."""
        print "Stats for player %s" % self.token
        print "  Throw count: %d" % self.throw_count
        print "  Hit/Miss: %d (%f%%) %d (%f%%)" % (
            self.hit_count,
            (self.hit_count/self.throw_count) * 100,
            self.miss_count,
            (self.miss_count/self.throw_count) * 100
        )
        print "  Inkast: %d %d %d" % (self.inkast_count, self.rethrow_count, self.penalty_count)

