from card_processor import CardProcessor
from card_processor2 import CardProcessor2

class CardPlayProcessor:
    @staticmethod
    def process_card_play(game_engine, player, card_to_play):
        if card_to_play.card_type == "shield":
            CardProcessor2.process_shield_card(game_engine, player)
        elif card_to_play.card_type == "attack":
            CardProcessor2.process_attack_card(game_engine, player)
        elif card_to_play.card_type == "random":
            CardProcessor2.process_random_card(game_engine, player)
        elif card_to_play.card_type == "draw":
            CardProcessor2.process_draw_card(game_engine, player, card_to_play)
        elif card_to_play.card_type == "life steal":
            CardProcessor2.process_life_steal_card(game_engine, player)
        elif card_to_play.card_type == "star":
            CardProcessor2.process_star_card(game_engine, player)
        elif card_to_play.card_type == "stop":
            CardProcessor2.process_stop_card(game_engine, player)
        elif card_to_play.card_type == "dragon":
            CardProcessor2.process_dragon_card(game_engine, player, card_to_play)
        elif card_to_play.card_type == "thunder":  # Check for thunder card
            CardProcessor2.process_thunder_card(game_engine, player, 3)  # Example: Destroy 3 creature cards
        else:
            CardProcessor.process_card_play(game_engine, player, card_to_play)
