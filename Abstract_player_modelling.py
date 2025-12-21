from pyomo.environ import *



class Player_abstract_model: 
    """
    Abstract model for a game with multiple players.
    Each player has a price and a revenue.
    """

    def __init__(self):
        # Create the abstract model
        self.model = AbstractModel()

        # Define the sets
        self.model.players = Set()  # Set of players

        # Define the parameters for price and revenue for each player
        self.model.price = Param(self.model.players, within=PositiveReals)
        self.model.revenue = Param(self.model.players, within=PositiveReals)
        self.model.time = Param(self.model.players, within=PositiveReals)

        # Define the decision variables for demand, indexed by players
        self.model.demand = Var(self.model.players, within=NonNegativeReals)
        
                # Define the objective: maximize total demand across all players
        def objective_rule(model):
            return sum(model.demand[p] for p in model.players)

        self.model.objective = Objective(rule=objective_rule, sense=maximize)

        # Define the revenue constraint: demand * price should be less than or equal to revenue
        def revenue_rule(model, p):
            return model.demand[p] * model.price[p] <= model.revenue[p]

        self.model.revenue_constraint = Constraint(self.model.players, rule=revenue_rule)



        
    def run_model(self, data):
        
        instance = self.model.create_instance(data)
        instance.pprint()


        # Solver setup (GLPK is used here)
        solver = SolverFactory('glpk')

        # Solve the model
        solver.solve(instance)
        print("Results for each player:")
        for player in instance.players:
            print(f"Player {player}:")
            print(f"  Demand: {instance.demand[player].value}")
            print(f"  Price: {instance.price[player]}")
            print(f"  Revenue: {instance.revenue[player]}")
            print("-------------------------")

      