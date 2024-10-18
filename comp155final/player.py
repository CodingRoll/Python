class Player:
    def __init__(self, name,):
        self.name = name
        self.hand = []
        self.life_points = 20
        

    def draw_card(self, card):
        if card is not None:  # Check if the drawn card is not None
            self.hand.append(card)
            print(f"{self.name} drew a card: {card}")
        else:
            print("Cannot draw a card from an empty deck.")

    def display_hand(self):
        print(f"{self.name}'s Hand:")
        for card in self.hand:
            print(card)
