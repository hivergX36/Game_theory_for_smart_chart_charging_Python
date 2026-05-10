from Agent_class_aggregator import aggregator
from Agent_class_player_type_1 import player_type_1
from Agent_class_player_type_2 import player_type_2
from Abstract_player_modelling_type_1 import Player_abstract_model_type_1
from Abstract_player_modelling_type_2 import Player_abstract_model_type_2
from Agent_class_controler import controler

# Sample data for players, prices, and revenues
NUMBER_ITER = 50
Epsilon = 10 ^ -6

# Admm criteria
step = 0.01
eps = 1
num_iter = 0

# Create and run the model
game_controller = controler(number_of_agent_type_1=10, number_of_agent_type_2=10)
game_controller.read_data_player_type_1("data_player_type_1.txt")
game_controller.read_data_player_type_2("data_player_type_2.txt")
game_controller.read_data_aggregator("data_aggregator.txt")

# Print agent programs by the controler

model_type_1 = Player_abstract_model_type_1()
model_type_2 = Player_abstract_model_type_2()

while eps > Epsilon and num_iter < NUMBER_ITER:
    for agent in game_controller.agent_list_type_1:
        agent.make_instance()
        model_type_1.run_model(agent.instance)
    for agent in game_controller.agent_list_type_2:
        agent.make_instance()
        model_type_2.run_model(agent.instance)
    for 
    game_controller.aggregator.make_instance(
        game_controller.agent_list_type_1, game_controller.agent_list_type_2
    )
    game_controller.aggregator.run_model()
