from Agent_class_aggregator import aggregator
from Agent_class_player_type_1 import player_type_1
from Agent_class_player_type_2 import player_type_2
from Abstract_player_modelling_type_1 import Player_abstract_model_type_1
from Abstract_player_modelling_type_2 import Player_abstract_model_type_2
from Agent_class_controler import controler

# Sample data for players, prices, and revenues

# Create and run the model
game_controller = controler(number_of_agent_type_1=10, number_of_agent_type_2=10)
game_controller.read_data_player_type_1("data_player_type_1.txt")
game_controller.read_data_player_type_2("data_player_type_2.txt")
game_controller.read_data_aggregator("data_aggregator.txt")

# Print agent programs by the controler
game_controller.print_controler()
game_controller.make_instance()
game_controller.print_instance()

model_type_1 = Player_abstract_model_type_1()
model_type_1.run_model(game_controller.agent_list_type_1[0].instance)
