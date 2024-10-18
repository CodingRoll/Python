class CardPlayer:
    def __init__(self, game_engine):
        self.game_engine = game_engine

    def play_card(self, player):
        print(f"\n{player.name}'s Turn:")
        print("Your Hand:")
        for i, card in enumerate(player.hand):
            print(f"{i+1}. {card} Cost: {card.cost}")

        while True:
            choice = input("Enter the number of the card you want to play (or enter 0 to end turn): ")
            if choice.isdigit() and 0 <= int(choice) <= len(player.hand):
                if int(choice) == 0:
                    print(f"{player.name} ended their turn.")
                    break

                card_index = int(choice) - 1
                card_to_play = player.hand[card_index]
                player_resources = self.game_engine.player1_resources if player == self.game_engine.player1 else self.game_engine.player2_resources

                if player_resources >= card_to_play.cost:
                    if player == self.game_engine.player1:
                        self.game_engine.player1_resources -= card_to_play.cost
                    else:
                        self.game_engine.player2_resources -= card_to_play.cost
                    player.hand.pop(card_index)
                    self.game_engine.process_card_play(player, card_to_play)
                    break
                else:
                    print("Sorry, you don't have enough resources to play this card.")
            else:
                print("Invalid input. Please enter a number between 0 and the number of cards in your hand.")