import itertools
from enum import Enum
from random import shuffle
class Deck:

    class DistributionStrategy(Enum):
        OneOne = 1
        OneThree = 2
        FiveFourFour = 3

    def __init__(self):
        self.cards = list(i for i in range (1,53,1))
        self.distribution_strategies = {
            Deck.DistributionStrategy.OneOne: self.one_one,
            Deck.DistributionStrategy.OneThree: self.one_three,
            Deck.DistributionStrategy.FiveFourFour: self.five_four_four
        }

    def shuffle(self):
        shuffle(self.cards)

    def distribute(self, distribution_strategy=DistributionStrategy.OneOne):
        return self.distribution_strategies[distribution_strategy]()

    def one_one(self):
        return list(self.cards[i::4] for i in range(4))

    def one_three(self):
        return list(self.cards[i * 13: (i + 1) * 13] for i in range(4))

    def five_four_four(self):
        return list(
            self.cards[i * 5: (i + 1) * 5]+
            self.cards[20 + (i * 4): 24 + (i * 4)]+
            self.cards[36 + (i * 4): 40 + (i * 4)]
         for i in range(4))
