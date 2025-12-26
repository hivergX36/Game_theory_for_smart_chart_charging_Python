from Agent_class_aggregator import aggregator
from Agent_class_player import player
from Abstract_player_modelling import Player_abstract_model
from Agent_class_controler import controler

# Sample data for players, prices, and revenues
data = {
    "players": {1, 2, 3},
    "price": {1: 10.0, 2: 15.0, 3: 20.0},
    "revenue": {1: 100.0, 2: 150.0, 3: 200.0},
    "time": {1: 1.0, 2: 1.5, 3: 2.0},
}

# Create and run the model
game_controller = controler(number_of_agent=10)
game_controller.read_data_player("data_player.txt")
game_controller.read_data_aggregator("data_aggregator.txt")
game_controller.print_controler()
