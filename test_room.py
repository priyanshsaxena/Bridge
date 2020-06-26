from user import User
from room import room
import unittest
import random
random.seed(50)


class RoomTest(unittest.TestCase):
    user1 = User("harshit")
    user2 = User("mukul")
    user3 = User("ankit")
    user4 = User("mayank")
    room1 = room(user1, user2, user3, user4)

    def test_method1(self):
        shuffled_deck = self.room1.deck.cards
        assert shuffled_deck == [17, 19, 39, 47, 48, 43,
                                 33, 38, 5, 51, 4, 2, 12,
                                 40, 52, 9, 25, 8, 1, 26, 29,
                                 27, 50, 46, 34, 14, 30, 20, 11,
                                 28, 3, 13, 49, 42, 37, 7, 23, 10,
                                 44, 36, 15, 21, 35, 6, 22, 31, 45,
                                 16, 41, 24, 18, 32]
        assert self.room1.player[room.players.p1].name == "harshit"
        assert self.room1.player[room.players.p2].name == "mukul"
        assert self.room1.player[room.players.p3].name == "ankit"
        assert self.room1.player[room.players.p4].name == "mayank"
        assert self.room1.player[room.players.p1].cards == shuffled_deck[0::4]
        assert self.room1.player[room.players.p2].cards == shuffled_deck[1::4]
        assert self.room1.player[room.players.p3].cards == shuffled_deck[2::4]
        assert self.room1.player[room.players.p4].cards == shuffled_deck[3::4]
        self.room1.user_bidding(room.players.p1, 3, 5, room.bid_status.Bid)
        assert self.room1.highest_bidder == room.players.p1
        self.room1.user_bidding(
            room.players.p2, None, None, room.bid_status.Double)
        self.room1.user_bidding(
            room.players.p3, None, None, room.bid_status.Double)
        self.room1.user_bidding(
            room.players.p4, None, None, room.bid_status.Pass)
        assert self.room1.highest_bidder == room.players.p1
        assert self.room1.doubles == 2
        assert self.room1.passes == 1
        assert self.room1.trump_card == 3
        assert self.room1.contract == 5
        self.room1.update_cards(room.players.p2, 19)
        assert self.room1.player[room.players.p2].cards == shuffled_deck[5::4]
        self.room1.update_score(room.players.p2)
        assert self.room1.score_table[room.Teams.Blue] == 0
        assert self.room1.score_table[room.Teams.Red] == 1
