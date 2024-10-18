class PlayingBoard:
    def __init__(self):
        self.player1_field = []
        self.player2_field = []

    def add_card_to_player1_field(self, card):
        self.player1_field.append(card)

    def add_card_to_player2_field(self, card):
        self.player2_field.append(card)

    def display_board(self):
        print("\n--------------------------------------------")
        print("Player 2's Field:")
        for card in self.player2_field:
            print(card.emoji, end=" ")
        print("\n--------------------------------------------")
        print("Player 1's Field:")
        for card in self.player1_field:
            print(card.emoji, end=" ")
        print("\n--------------------------------------------")