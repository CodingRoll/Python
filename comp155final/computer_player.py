from random import choice

class ComputerPlayer:
    def play_card(self, player, game_engine):
        print("\nComputer's Turn:")
        print("Computer's Hand:")
        for i, card in enumerate(player.hand):
            print(f"{i+1}. {card} Cost: {card.cost}")

        playable_cards = [card for card in player.hand if self.can_play_card(card, player, game_engine)]
        
        if playable_cards:
            card_to_play = choice(playable_cards)
            player.hand.remove(card_to_play)
            game_engine.process_card_play(player, card_to_play)
            print(f"Computer played {card_to_play}")
        else:
            print("Computer doesn't have any playable cards. Ending turn.")

    def can_play_card(self, card, player, game_engine):
        player_resources = game_engine.player2_resources if player == game_engine.player2 else game_engine.player1_resources
        return player_resources >= card.cost