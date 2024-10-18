from play_cards import CardPlayer

class TurnSimulator:
    def __init__(self, game_engine):
        self.game_engine = game_engine
    
    def simulate_turn(self, player):
        self.game_engine.current_player = player
        while True:
            self.game_engine.display_resources_and_life()  # Show resources and life points at the start of the turn
            # Increment player's resources by one at the start of every turn
            if player == self.game_engine.player1:
                self.game_engine.player1_resources += 1
            else:
                self.game_engine.player2_resources += 1
            
            player.draw_card(self.game_engine.deck.draw_card())  # Draw a card at the beginning of the turn
            
            if hasattr(player, 'computer'):
                player.computer.play_card(player, self.game_engine)  # Computer player's turn
            else:
                card_player = CardPlayer(self.game_engine)
                card_player.play_card(player)  # Human player's turn
            
            self.game_engine.playing_board.display_board()

            opponent = self.game_engine.player2 if player == self.game_engine.player1 else self.game_engine.player1
            if not hasattr(player, 'computer') or not hasattr(opponent, 'computer'):
                choice = input("Press Enter to end your turn. Press 1 to keep playing cards: ")
                if choice == "":
                    break
            else:
                break