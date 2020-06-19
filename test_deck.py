import unittest

from deck import Deck
import random

class DeckTest(unittest.TestCase):

    deck1 = Deck()
    def test_method1(self):
        random.seed(50)
        self.deck1.shuffle()
        shuffled_deck = self.deck1.cards
        assert shuffled_deck == [17, 19, 39, 47, 48, 43, 33, 38, 5, 51, 4, 2, 12, 40, 52, 9, 25, 8, 1, 26, 29, 27, 50, 46, 34, 14, 30, 20, 11, 28, 3, 13, 49, 42, 37, 7, 23, 10, 44, 36, 15, 21, 35, 6, 22, 31, 45, 16, 41, 24, 18, 32]
        distributed_deck11 = self.deck1.distribute(distribution_strategy=Deck.DistributionStrategy.OneOne)
        assert len(distributed_deck11) == 4
        assert distributed_deck11 == list(shuffled_deck[i::4] for i in range (4))
        distributed_deck13 = self.deck1.distribute(distribution_strategy=Deck.DistributionStrategy.OneThree)
        assert len(distributed_deck13) == 4
        assert distributed_deck13 == list(shuffled_deck[i:i+13] for i in range(0,52,13))
        distributed_deck544 = self.deck1.distribute(distribution_strategy=Deck.DistributionStrategy.FiveFourFour)
        assert len(distributed_deck544) == 4
        assert distributed_deck544 == list(shuffled_deck[i*5:(i+1)*5]+shuffled_deck[20+i*4:24+i*4]+shuffled_deck[36+i*4:40+i*4] for i in range (4))



    deck2 = Deck()

    def test_method2(self):
        random.seed(15)
        self.deck2.shuffle()
        shuffled_deck = self.deck2.cards
        assert shuffled_deck == [36, 49, 5, 9, 29, 51, 44, 25, 27, 13, 39, 6, 33, 20, 45, 41, 21, 32, 19, 42, 52, 50, 43, 40, 47, 35, 12, 31, 7, 28, 38, 15, 37, 17, 26, 18, 23, 30, 22, 8, 46, 24, 10, 4, 2, 16, 11, 3, 48, 34, 1, 14]
        distributed_deck11 = self.deck2.distribute(distribution_strategy=Deck.DistributionStrategy.OneOne)
        assert len(distributed_deck11) == 4
        assert distributed_deck11 == list(shuffled_deck[i::4] for i in range (4))
        distributed_deck13 = self.deck2.distribute(distribution_strategy=Deck.DistributionStrategy.OneThree)
        assert len(distributed_deck13) == 4
        assert distributed_deck13 == list(shuffled_deck[i:i+13] for i in range(0,52,13))
        distributed_deck544 = self.deck2.distribute(distribution_strategy=Deck.DistributionStrategy.FiveFourFour)
        assert len(distributed_deck544) == 4
        assert distributed_deck544 == list(shuffled_deck[i*5:(i+1)*5]+shuffled_deck[20+i*4:24+i*4]+shuffled_deck[36+i*4:40+i*4] for i in range (4))
