from pyomo.environ import *

model_player = AbstractModel() 
model_player.demand = Var(within = PositiveReals)
model_player.revenue = Param(within = PositiveReals)
model_player.price = Param(within = PositiveReals)

#define objective function 

def objective_rule(model_player):
    return  - model_player.demand

model_player.value =  Objective( rule=objective_rule, sense=minimize )

#Define revenue constraint 

def revenue_rule(model_player):
    return model_player.price * model_player.demand  <= model_player.revenue 


model_player.revenue_const = Constraint(rule=revenue_rule)

