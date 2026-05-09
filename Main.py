from Agent_class_aggregator import aggregator
from Agent_class_player_type_1 import player
from Abstract_player_modelling_type_1 import Player_abstract_model
from Agent_class_controler import controler

# Sample data for players, prices, and revenues

# Create and run the model
game_controller = controler(number_of_agent=10)
game_controller.read_data_player("data_player.txt")
game_controller.read_data_aggregator("data_aggregator.txt")

# Print agent programs by the controler
game_controller.print_controler()
