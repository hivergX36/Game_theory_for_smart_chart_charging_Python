from Abstract_aggregator_modelling import Aggregator_abstract_model
from Agent_class_aggregator import aggregator
from Agent_class_player_type_1 import player_type_1
from Agent_class_player_type_2 import player_type_2
from Abstract_player_modelling_type_1 import Player_abstract_model_type_1
from Abstract_player_modelling_type_2 import Player_abstract_model_type_2
from Agent_class_controler import controler

# Sample data for players, prices, and revenues
NUMBER_ITER = 3
Epsilon = 10 ^ -6

# Admm criteria
step = 0.01
eps = 1
num_iter = 0
demand_all_player_type_1 = [0 for i in range(10)]
demand_all_player_type_2 = [0 for i in range(10)]
sum_demand_type_1 = 0
sum_demand_type_2 = 0

# Create and run the model
game_controller = controler(number_of_agent_type_1=10, number_of_agent_type_2=10,rho: 0.02,mu: 0.02)
game_controller.read_data_player_type_1("data_player_type_1.txt")
game_controller.read_data_player_type_2("data_player_type_2.txt")
game_controller.read_data_aggregator("data_aggregator.txt")

# Print agent programs by the controler

model_type_1 = Player_abstract_model_type_1()
model_type_2 = Player_abstract_model_type_2()
model_aggregator = Aggregator_abstract_model()

while eps > Epsilon and num_iter < NUMBER_ITER:

    # Creater instance for each player and run the model for each player
    num_iter += 1
    game_controller.make_player_instance()
    game_controller.player_instance()

    # Run model for each player and update the demand variable for each player

    for i, agent in enumerate(game_controller.agent_list_type_1):
        model_type_1.run_model(agent.instance)
        agent.variables["d"] = model_type_1.player_solution
        print("Player type 1: ", agent.name, "d: ", agent.variables["d"])
    for i, agent in enumerate(game_controller.agent_list_type_2):
        model_type_2.run_model(agent.instance)
        agent.variables["d"] = model_type_2.player_solution
        print("Player type 2: ", agent.name, "d: ", agent.variables["d"])
    game_controller.aggregator.get_all_demand(
        game_controller.agent_list_type_1, game_controller.agent_list_type_2
    )

    game_controller.make_aggregator_instance()
    model_aggregator.run_model(game_controller.aggregator.instance)
    game_controller.aggregator.variables["Q1"] = model_aggregator.Q1_solution
    game_controller.aggregator.variables["Q2"] = model_aggregator.Q2_solution
    print("Aggregator Q1: ", game_controller.aggregator.variables["Q1"])
    print("Aggregator Q2: ", game_controller.aggregator.variables["Q2"])
    game_controller.update_annother_demand_type_for_each_player()
    game_controller.update_aggregator_price()
    game_controller.update_player_type_price()
    


# Display results for each player and the aggregator

for i, agent in enumerate(game_controller.agent_list_type_1):
    agent.dislay_solution()
for i, agent in enumerate(game_controller.agent_list_type_2):
    agent.dislay_solution()
game_controller.aggregator.dislay_solution()
