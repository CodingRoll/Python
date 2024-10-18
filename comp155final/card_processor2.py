class CardProcessor2:
    @staticmethod
    def process_shield_card(game_engine, player):
        print(f"{player.name} played Shield ⛨ card")
        # Set the player's shield status to True, indicating invincibility
        player.shield_status = True

    @staticmethod
    def process_thunder_card(game_engine, player, creatures_to_destroy):
        print(f"{player.name} played Thunder ⚡️ card")

        opponent_field = game_engine.playing_board.player1_field if player == game_engine.player2 else game_engine.playing_board.player2_field
    
        remaining_cards = [card for card in opponent_field if card.card_type != "creature"]
        destroyed_cards = [card for card in opponent_field if card.card_type == "creature"][:creatures_to_destroy]
    
        if player == game_engine.player2:
            game_engine.playing_board.player1_field = remaining_cards
        else:
            game_engine.playing_board.player2_field = remaining_cards

        print(f"{len(destroyed_cards)} creature(s) destroyed from the opponent's field.")
    
        if player == game_engine.player2:
            game_engine.playing_board.player1_field = remaining_cards
        else:
            game_engine.playing_board.player2_field = remaining_cards


    @staticmethod
    def process_attack_card(game_engine, player):
        print(f"{player.name} played Attack 🗡️ card")
        # Deduct damage from the opponent player's life points
        opponent = game_engine.player2 if player == game_engine.player1 else game_engine.player1
        opponent.life_points -= 1

    @staticmethod
    def process_random_card(game_engine, player):
        print(f"{player.name} played Random 🌌 card")
        # Add a random card to the player's hand
        player.draw_card(game_engine.deck.draw_card())

    @staticmethod
    def process_draw_card(game_engine, player, card_to_play):
        print(f"{player.name} played Draw 🎴 card")
        # Determine the number of cards to draw based on the card's level
        if card_to_play.level == 1:
            num_cards_to_draw = 2
        elif card_to_play.level == 2:
            num_cards_to_draw = 3
        elif card_to_play.level == 3:
            num_cards_to_draw = 4
        else:
            num_cards_to_draw = 0  # Default to 0 cards if level is invalid

        # Draw the specified number of cards from the deck and add them to the player's hand
        for _ in range(num_cards_to_draw):
            drawn_card = game_engine.deck.draw_card()
            if drawn_card:
                player.draw_card(drawn_card)
            else:
                print("The deck is empty.")

    @staticmethod
    def process_life_steal_card(game_engine, player):
        print(f"{player.name} played Life Steal 🧛🏻 card")
        # Deduct 3 life points from the opponent and add them to the player's life points
        opponent = game_engine.player2 if player == game_engine.player1 else game_engine.player1
        if opponent.life_points >= 3:
            opponent.life_points -= 3
            player.life_points += 3
            print(f"{player.name} stole 3 life points from {opponent.name}")
        else:
            print("Not enough life points to steal from the opponent.")

    @staticmethod
    def process_star_card(game_engine, player):
        print(f"{player.name} played Star ☄️ card")
        game_engine.playing_board.player1_field = []  # Clear player 1's field
        game_engine.playing_board.player2_field = []  # Clear player 2's field

    @staticmethod
    def process_stop_card(game_engine, player):
        print(f"{player.name} played Stop 🚫 card")
        
        # Set the other player's stop status to True, indicating inability to play cards
        other_player = game_engine.player2 if player == game_engine.player1 else game_engine.player1
        other_player.stop_status = True

    @staticmethod
    def process_dragon_card(game_engine, player, card_to_play):
        print(f"{player.name} played Dragon 🐲 card")
        # Add the dragon card to the respective player's field
        if player == game_engine.player1:
            game_engine.playing_board.add_card_to_player1_field(card_to_play)
        else:
            game_engine.playing_board.add_card_to_player2_field(card_to_play)