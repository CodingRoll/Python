from player import Player
from deck import Deck
from playing_board import PlayingBoard
from turn_simulation import TurnSimulator
from computer_player import ComputerPlayer
from card_play_processor import CardPlayProcessor

class GameEngine:
    def __init__(self):
        self.deck = Deck()
        self.player1 = None
        self.player2 = None
        self.player1_resources = 10  # Assume starting resources for demonstration
        self.player2_resources = 10  # Assume starting resources for demonstration
        self.playing_board = PlayingBoard()
        self.current_player = None
        self.turn_simulator = TurnSimulator(self)  # Initialize turn simulator

    def setup_game(self):
        if self.player2.name == "Computer":
            self.player2.computer = ComputerPlayer()
    
        # Shuffle the deck
        self.deck.shuffle()

        # Draw initial hands for players
        for _ in range(5):
            self.player1.draw_card(self.deck.draw_card())
            self.player2.draw_card(self.deck.draw_card())

        # Additional setup for one player vs computer game mode
        if self.player2.name == "Computer":
            self.player2.computer = ComputerPlayer()  # Initialize the computer player

    def display_resources_and_life(self):
        # Display the current resources and life points of both players
        print(f"\nPlayer 1 Resources: {self.player1_resources} | Life Points: {self.player1.life_points}")
        print(f"Player 2 Resources: {self.player2_resources} | Life Points: {self.player2.life_points}\n")

    def process_card_play(self, player, card_to_play):
            CardPlayProcessor.process_card_play(self, player, card_to_play)
            

    def select_opponents(self):
        print("Welcome to the card game!")
        print("Select an option:")
        print("1. Player vs Player")
        print("2. Player vs Computer")

        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                self.player1 = Player(input("Enter Player 1's name: "))
                self.player2 = Player(input("Enter Player 2's name: "))
                break
            elif choice == "2":
                self.player1 = Player(input("Enter your name: "))
                self.player2 = Player("Computer")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def end_turn(self):
        # Deal damage from creature cards on the playing field
        for creature in self.playing_board.player1_field:
            self.player2.life_points -= creature.level
        for creature in self.playing_board.player2_field:
            self.player1.life_points -= creature.level

    def start_game(self):
        self.select_opponents()
        self.setup_game()
        while True:
            self.turn_simulator.simulate_turn(self.player1)
            self.end_turn()
            self.turn_simulator.simulate_turn(self.player2)
            self.end_turn()
            
            # Check if player 1 has drawn the last card
            if len(self.deck.cards) == 0:
                print(f"{self.player1.name} wins by drawing the last card!")
                break
            
            # Simulate Player 2's turn
            self.turn_simulator.simulate_turn(self.player2)
            # Reset shield status after one turn
            self.player2.shield_status = False
            
            # Check if player 2 has drawn the last card
            if len(self.deck.cards) == 0:
                print(f"{self.player2.name} wins by drawing the last card!")
                break
            
            # Check for life points win condition
            if self.player1.life_points <= 0:
                print(f"{self.player2.name} wins!")
                break
            elif self.player2.life_points <= 0:
                print(f"{self.player1.name} wins!")
                break