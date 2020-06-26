from enum import Enum
from deck import Deck


class room:
    class players(Enum):
        p1 = 1
        p2 = 2
        p3 = 3
        p4 = 4

    class Teams(Enum):
        Blue = 1
        Red = 2

    class bid_status(Enum):
        Pass = 1
        Double = 2
        Bid = 3

    def __init__(self, user1, user2, user3, user4):
        self.player = {
            self.players.p1: user1,
            self.players.p2: user2,
            self.players.p3: user3,
            self.players.p4: user4
        }
        self.highest_bidder = None
        self.current_bidder = None
        self.trump_card = None
        self.current_trump = None
        self.contract = None
        self.current_contract = None
        self.passes = 0  # when passes reaches to 3 bis is finalized
        self.doubles = 0
        self.bid_functions = {
            room.bid_status.Pass: self.set_pass,
            room.bid_status.Double: self.set_double,
            room.bid_status.Bid: self.set_bid
        }
        self.deck = Deck()
        self.deck.shuffle()

        cards_distributed = self.deck.distribute()
        self.teammates = {
            self.players.p1: self.players.p3,
            self.players.p2: self.players.p4,
            self.players.p3: self.players.p1,
            self.players.p4: self.players.p2
        }
        self.teams = {
            self.players.p1: self.Teams.Blue,
            self.players.p2: self.Teams.Red,
            self.players.p3: self.Teams.Blue,
            self.players.p4: self.Teams.Red
        }
        self.player[self.players.p1].set_cards(cards_distributed[0])
        self.player[self.players.p2].set_cards(cards_distributed[1])
        self.player[self.players.p3].set_cards(cards_distributed[2])
        self.player[self.players.p4].set_cards(cards_distributed[3])

        self.score_table = {
            self.Teams.Blue: 0,
            self.Teams.Red: 0
        }

    def set_pass(self):
        self.passes += 1

    def set_double(self):
        self.doubles += 1

    def set_bid(self):
        self.passes = 0
        self.doubles = 0
        self.highest_bidder = self.current_bidder
        self.trump_card = self.current_trump
        self.contract = self.current_contract

    def user_bidding(self, player_id, trump_card, contract, status):
        self.current_bidder = player_id
        self.current_trump = trump_card
        self.current_contract = contract
        return self.bid_functions[status]()

    def update_cards(self, player_id, card):
        self.player[player_id].update_cards(card)

    def update_score(self, player_id):
        self.score_table[self.teams[player_id]] += 1
