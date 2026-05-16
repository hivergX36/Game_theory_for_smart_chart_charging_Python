from Abstract_aggregator_modelling import Aggregator_abstract_model
from Agent_class_aggregator import aggregator
from Agent_class_player_type_1 import player_type_1
from Agent_class_player_type_2 import player_type_2
from Abstract_player_modelling_type_1 import Player_abstract_model_type_1
from Abstract_player_modelling_type_2 import Player_abstract_model_type_2
from Agent_class_controler import controler

# Sample data for players, prices, and revenues
NUMBER_ITER = 100
Epsilon_primal = 10**-6
Epsilon_dual = 10**-6

# Admm criteria
step = 0.02
eps_primal = 10
eps_dual = 100
num_iter = 0
demand_all_player_type_1 = [0 for i in range(1)]
demand_all_player_type_2 = [0 for i in range(1)]
sum_demand_type_1 = 0
sum_demand_type_2 = 0

# Create and run the model
game_controller = controler(
    number_of_agent_type_1=1, number_of_agent_type_2=1, rho=0.1, mu=0.1
)
game_controller.read_data_player_type_1("data_player_type_1.txt")
game_controller.read_data_player_type_2("data_player_type_2.txt")
game_controller.read_data_aggregator("data_aggregator.txt")

# Print agent programs by the controler

model_type_1 = Player_abstract_model_type_1()
model_type_2 = Player_abstract_model_type_2()
model_aggregator = Aggregator_abstract_model()

while (
    num_iter < NUMBER_ITER and eps_primal > Epsilon_primal and eps_dual > Epsilon_dual
):

    # Creater instance for each player and run the model for each player
    num_iter += 1
    game_controller.make_player_instance()
    game_controller.player_instance()

    # Run model for each player and update the demand variable for each player

    for i, agent in enumerate(game_controller.agent_list_type_1):
        model_type_1.run_model(agent.instance)
        agent.variables["d"] = model_type_1.player_solution
        print("Player type 1: ", agent.name, "demand: ", agent.variables["d"])
    for i, agent in enumerate(game_controller.agent_list_type_2):
        model_type_2.run_model(agent.instance)
        agent.variables["d"] = model_type_2.player_solution
        print("Player type 2: ", agent.name, "demand: ", agent.variables["d"])
    game_controller.update_demand_all_list_with_sum()
    game_controller.update_another_demand_type_for_each_player()
    print("controller variables: ", game_controller.aggregator.variables)
    game_controller.make_aggregator_instance()
    print("controler aggregator instance: ", game_controller.aggregator.instance)
    model_aggregator.run_model(game_controller.aggregator.instance)
    print("Aggregator Q1 solution: ", model_aggregator.Q1_solution)
    print("Aggregator Q2 solution: ", model_aggregator.Q2_solution)
    game_controller.aggregator.variables["Q1"] = model_aggregator.Q1_solution
    game_controller.aggregator.variables["Q2"] = model_aggregator.Q2_solution
    print("Aggregator Q1: ", game_controller.aggregator.variables["Q1"])
    print("Aggregator Q2: ", game_controller.aggregator.variables["Q2"])
    game_controller.update_aggregator_price()
    game_controller.update_player_type_price()
    game_controller.update_player_quantity_distributed()
    game_controller.update_history()
    eps_primal = game_controller.compute_eps_primal()
    eps_dual = game_controller.compute_eps_dual()
    print("eps_primal: ", eps_primal)
    print("eps_dual: ", eps_dual)
# Display results for each player and the aggregator

for i, agent in enumerate(game_controller.agent_list_type_1):
    print("Player type 1: ")
    agent.dislay_solution()
    agent.display_variables()
for i, agent in enumerate(game_controller.agent_list_type_2):
    print("Player type 2: ")
    agent.dislay_solution()
    agent.display_variables()
game_controller.aggregator.dislay_solution()
print("eps_primal: ", eps_primal)
print("eps_dual: ", eps_dual)
