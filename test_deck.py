import unittest

from deck import Deck


class DeckTest(unittest.TestCase):

    deck = Deck()

    def test_method1(self):
        shuffled_deck = self.deck.distribute(distribution_strategy=Deck.DistributionStrategy.OneOne)
        assert len(shuffled_deck) == 4
        assert shuffled_deck[0] == list(range(0, 52, 4))
