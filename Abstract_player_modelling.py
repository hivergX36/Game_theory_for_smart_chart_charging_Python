from pyomo.environ import *



class Player_abstract_model: 
    """
    Abstract class for player modelling in a game.
    This class defines the basic structure and variables for a player model.
    """

    def __init__(self):
        
        self.model = AbstractModel()
        self.model.demand = Var(within=PositiveReals)
        self.revenue = Param(within=PositiveReals)
        self.price = Param(within=PositiveReals)
        
        
        def objective_rule(model_player):
            return model_player.demand
        
        self.model.objective = Objective(rule=objective_rule, sense=maximize)

        #Define revenue constraint
        def revenue_rule(model_player):
            return model_player.price * model_player.demand  <= model_player.revenue

        self.model.revenue_const = Constraint(rule=revenue_rule)
        
    def run_model(self, data):
        
        self.model.price = Param(initialize=data['price'], within=PositiveReals)
        self.model.revenue = Param(initialize=data['revenue'], within=PositiveReals)
        self.model.pprint()
        instance = self.model.create_instance(data)
        solver = SolverFactory('glpk')
        solver.solve(instance)
        print(f"Results for the Player:")
        print(f"Demand: {instance.demand.value}")
        print(f"Price: {instance.price.value}")
        print(f"Revenue: {instance.revenue.value}")

      




