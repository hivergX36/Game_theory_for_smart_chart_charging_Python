from pyomo.environ import *


class Player_abstract_model_type_2:
    """
    Abstract model for a game with multiple players.
    Each player has a price and a revenue.
    """

    """ print("Agent name: ", self.name)
        print("Agent program: ")
        print("Agent type: ", self.program["type"])
        print("max d1")
        print("subject to: ", "lambda_f1 * d1 <= " + str(self.program["revenue"]))
        print("d1 <= " + str(self.program["max_demand"]))
        if self.program["type"] == 1:
            print("sum_demand_type_1 + 1/t <= " + "Q")
        else:
            print("sum_demand_type_1 +sum_demand_type_2 + 1/t <= " + "Q")

    """

    def __init__(self):
        # Create the abstract model
        self.model = AbstractModel()

        # Define the sets
        self.model.players = Set()  # Set of players

        # Define the parameters for price and revenue for each player
        self.model.price = Param(within=PositiveReals)
        self.model.r = Param(within=PositiveReals)
        self.model.debit_time = Param(within=PositiveReals)
        self.model.provider_quantity = Param(within=PositiveReals)

        # Define the decision variables for demand, indexed by players
        self.model.demand = Var(self.model.players, within=NonNegativeReals)

        # Define the objective: maximize total demand across all players
        def objective_rule(model):
            return sum(model.demand[p] for p in model.players)

        self.model.objective = Objective(rule=objective_rule, sense=maximize)

        # Define the revenue constraint: demand * price should be less than or equal to revenue
        def revenue_rule(model, p):
            return model.demand[p] * model.price[p] <= model.revenue[p]

        self.model.revenue_constraint = Constraint(
            self.model.players, rule=revenue_rule
        )

    def run_model(self, data):

        instance = self.model.create_instance(data)
        instance.pprint()

        # Solver setup (GLPK is used here)
        solver = SolverFactory("glpk")

        # Solve the model
        solver.solve(instance)
        print("Results for each player:")
        for player in instance.players:
            print(f"Player {player}:")
            print(f"  Demand: {instance.demand[player].value}")
            print(f"  Price: {instance.price[player]}")
            print(f"  Revenue: {instance.revenue[player]}")
            print("-------------------------")
