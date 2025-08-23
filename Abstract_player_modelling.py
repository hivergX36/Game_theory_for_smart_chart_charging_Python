from pyomo.environ import *



class Player_astract_model: 
    """
    Abstract class for player modelling in a game.
    This class defines the basic structure and variables for a player model.
    """

    def __init__(self):
        
        self.model = AbstractModel()
        self.demand = Var(within=PositiveReals)
        self.revenue = Param(within=PositiveReals)
        self.price = Param(within=PositiveReals)
        
        
        def objective_rule(model_player):
            return model_player.demand
        
        self.model.objective = Objective(rule=objective_rule, sense=minimize)

        #Define revenue constraint
        def revenue_rule(model_player):
            return model_player.price * model_player.demand  <= model_player.revenue

        self.model.revenue_const = Constraint(rule=revenue_rule)




