from pyomo.environ import *

class GameModel:
    """
    Abstract model for a game with multiple players.
    Each player has a price and a revenue.
    """

    def __init__(self):
        # Create the abstract model
        self.model = AbstractModel()

        # Define the sets for players (This needs to be declared here)
        self.model.players = Set()

        # Define parameters for price and revenue for each player
        self.model.price = Param(self.model.players, within=PositiveReals)
        self.model.revenue = Param(self.model.players, within=PositiveReals)

        # Define decision variables for demand, indexed by players
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
        """
        Run the optimization model with the provided data (prices, revenues, etc. for players).
        """

        # Create the model instance using the provided data
        instance = self.model.create_instance(data)

        # Print out the model instance to debug
        print("Model Instance (using pprint):")
        instance.pprint()

        # Display Sets (players)
        print("\nPlayers Set:")
        for player in instance.players:
            print(player)

        # Display Parameters (price and revenue)
        print("\nPrice for each player:")
        for player in instance.players:
            print(f"Player {player}: {instance.price[player]}")

        print("\nRevenue for each player:")
        for player in instance.players:
            print(f"Player {player}: {instance.revenue[player]}")

        # Display Variables (demand)
        print("\nDemand for each player:")
        for player in instance.players:
            print(f"Player {player}: {instance.demand[player].value if instance.demand[player].value is not None else 'Not Set'}")

        # Solver setup (GLPK is used here)
        solver = SolverFactory('glpk')

        # Solve the model
        results = solver.solve(instance, tee=True)  # tee=True to print solver output

        # Check the solver status
        print(f"\nSolver Status: {results.solver.status}")
        print(f"Solver Termination Condition: {results.solver.termination_condition}")

        # Output the results for each player
        print("\nResults for each player:")

        # Print the demand variable values for each player
        for player in instance.players:
            print(f"Player {player}:")
            print(f"  Demand: {instance.demand[player].value if instance.demand[player].value is not None else 'Not Set'}")
            print(f"  Price: {instance.price[player]}")
            print(f"  Revenue: {instance.revenue[player]}")
            print("-------------------------")

# Sample data for players, prices, and revenues
data = {
    None:{
    'players': ['P1', 'P2'],  # List of players
    'price': {'P1': 10, 'P2': 15},  # Prices for each player
    'revenue': {  # Revenue for each player
        'P1': 100,
        'P2': 120,
    }
    }
    
}

# Create and run the model
game_model = GameModel()
game_model.run_model(data)
