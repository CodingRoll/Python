import random

class Card:
    def __init__(self, card_type, level, emoji, cost, damage=0):
        self.card_type = card_type
        self.level = level
        self.emoji = emoji
        self.cost = cost
        self.damage = damage

    def __str__(self):
        if self.card_type == "creature":
            return f"{self.card_type} {self.level} {self.emoji} (Damage: {self.damage})"
        else:
            return f"{self.card_type} {self.level} {self.emoji}"


class Deck:
    def __init__(self):
        self.cards = []
        self.populate_deck()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            print("Deck is empty.")
            return None

    def populate_deck(self):
        card_data = [
            {"type": "creature", "emojis": ["😺", "😺😺", "😺😺😺"], "costs": [1, 2, 3], "damage": [1, 2, 3]},
            {"type": "resource", "emojis": ["⌛", "⌛⌛", "⌛⌛⌛"], "costs": [-1, -2, -3]},
            {"type": "spell", "emojis": ["🔮", "🔮🔮", "🔮🔮🔮"], "costs": [1, 2, 3]},
            {"type": "equipment", "emojis": ["⚔️", "⚔️⚔️", "⚔️⚔️⚔️"], "costs": [1, 2, 3]},
            {"type": "thunder", "emojis": ["⚡️"], "costs": [5]}, # destroys creatures 
            {"type": "shield", "emojis": ["⛨"], "costs": [1]}, # makes you invincible for one turn.
            {"type": "attack", "emojis": ["🗡️"], "costs": [0], "damage": [1]}, # makes you deal 1 damage to the enemy.
            {"type": "random", "emojis": ["🌌"], "costs": [3]}, # adds a random card to your hand, ignoring 'adds card' attribute for now.
            {"type": "draw", "emojis": ["🎴", "🎴🎴" , "🎴🎴🎴",], "costs": [5, 6, 8,]}, # draws 2 , 3, 4 cards from the deck, ignoring 'cards' attribute for now.
            {"type": "life steel", "emojis": ["🧛🏻"], "costs": [3]},#takes 3 life points from other player give it to your self.
            {"type": "star", "emojis": ["☄️"], "costs": [3]},# clears the play field, like thunder but dose it for both fields
            {"type": "stop", "emojis": ["🚫"], "costs": [6]}, #prevents other player from playing any card for 1 turns.
            {"type": "dragon", "emojis": ["🐲", "🐲🐲", "🐲🐲🐲"], "costs": [1, 2, 3], "damage": [1, 2, 3]}, # deals damge when on fild = to damage can only be removed by star             
        ]

        total_cards = 40  # Total number of cards in the deck
        cards_added = 0

        while cards_added < total_cards:
            for data in card_data:
                card_type = data["type"]
                emojis = data["emojis"]
                costs = data["costs"]
                damages = data.get("damage", [0] * len(emojis))  # Default damage to 0 if not specified
                for i, emoji in enumerate(emojis):
                    if cards_added >= total_cards:
                        break
                    cost = costs[i]
                    damage = damages[i] if i < len(damages) else 0  # Ensure damage index exists
                    card = Card(card_type, i + 1, emoji, cost, damage)
                    self.add_card(card)
                    cards_added += 1

        self.shuffle()