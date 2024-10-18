class CardProcessor:
    @staticmethod
    def process_card_play(game_engine, player, card_to_play):
        print(f"{player.name} played {card_to_play}")
        if card_to_play.card_type == "creature":
            if player == game_engine.player1:
                game_engine.playing_board.add_card_to_player1_field(card_to_play)
            else:
                game_engine.playing_board.add_card_to_player2_field(card_to_play)
        elif card_to_play.card_type == "resource":
            if player == game_engine.player1:
                game_engine.player1_resources += card_to_play.cost
            else:
                game_engine.player2_resources += card_to_play.cost
        elif card_to_play.card_type == "spell":
            if card_to_play.level == 1:
                damage = 1
            elif card_to_play.level == 2:
                damage = 2
            elif card_to_play.level == 3:
                damage = 3
            else:
                damage = 0  # Default to 0 damage if level is invalid
            
            if player == game_engine.player1:
                game_engine.player2.life_points -= damage  # Deduct damage from player 2
            else:
                game_engine.player1.life_points -= damage  # Deduct damage from player 1
        elif card_to_play.card_type == "equipment":
            if card_to_play.level == 1:
                boost = 1
            elif card_to_play.level == 2:
                boost = 2
            elif card_to_play.level == 3:
                boost = 3
            else:
                boost = 0  # Default to 0 boost if level is invalid
            
            if player == game_engine.player1:
                game_engine.player1.life_points += boost  # Boost life points of player 1
            else:
                game_engine.player2.life_points += boost  # Boost life points of player 2
        
        # Deal damage per turn for each creature on the field
        for creature in game_engine.playing_board.player1_field + game_engine.playing_board.player2_field:
            if creature.card_type == "creature":
                damage = creature.level  # Damage corresponds to creature's level
                if creature in game_engine.playing_board.player1_field:
                    game_engine.player2.life_points -= damage  # Deduct damage from player 2
                else:
                    game_engine.player1.life_points -= damage  # Deduct damage from player 1
        