class User:
    def __init__(self, name):
        self.name = name
        self.cards = None

    def set_cards(self, cards):
        self.cards = cards

    def update_cards(self, card):
        self.cards.remove(card)
