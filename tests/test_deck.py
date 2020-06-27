import random

import pytest

from app.deck import Deck

test_data_shuffled_decks = [
    (50, [17, 19, 39, 47, 48, 43, 33, 38, 5, 51, 4, 2, 12,
          40, 52, 9, 25, 8, 1, 26, 29, 27, 50, 46, 34, 14,
          30, 20, 11, 28, 3, 13, 49, 42, 37, 7, 23, 10, 44,
          36, 15, 21, 35, 6, 22, 31, 45, 16, 41, 24, 18, 32]),
    (15, [36, 49, 5, 9, 29, 51, 44, 25, 27, 13, 39, 6, 33,
          20, 45, 41, 21, 32, 19, 42, 52, 50, 43, 40, 47, 35,
          12, 31, 7, 28, 38, 15, 37, 17, 26, 18, 23, 30, 22,
          8, 46, 24, 10, 4, 2, 16, 11, 3, 48, 34, 1, 14])
]


@pytest.mark.parametrize(
    "seed, expected_shuffled_deck", test_data_shuffled_decks
)
def test_one_one(seed, expected_shuffled_deck):
    routine(Deck(), seed, Deck.DistributionStrategy.OneOne,
            list(
                expected_shuffled_deck[i::4] for i in range(4)))


@pytest.mark.parametrize(
    "seed, expected_shuffled_deck", test_data_shuffled_decks
)
def test_one_three(seed, expected_shuffled_deck):
    routine(Deck(), seed, Deck.DistributionStrategy.OneThree,
            list(
                expected_shuffled_deck[i:i+13] for i in range(0, 52, 13)))


@pytest.mark.parametrize(
    "seed, expected_shuffled_deck", test_data_shuffled_decks
)
def test_five_four_four(seed, expected_shuffled_deck):
    routine(Deck(), seed, Deck.DistributionStrategy.FiveFourFour,
            list(
                expected_shuffled_deck[i * 5: (i + 1) * 5] +
                expected_shuffled_deck[20+i * 4: 24 + i * 4] +
                expected_shuffled_deck[36 + i * 4: 40 + i * 4]
                for i in range(4)))


def routine(deck, seed, distribution_strategy, expected_distribution):
    random.seed(seed)
    deck.shuffle()
    distributed_deck = deck.distribute(
        distribution_strategy=distribution_strategy)
    assert distributed_deck == expected_distribution
    return deck.cards
