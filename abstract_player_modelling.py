from pyomo.environ import *

model_player = AbstractModel() 

model_player.demand = Var(within = PositiveReals)
model_player.revenue = Param(within = PositiveReals)
model_player.price = Param(within = PositiveReals)

#define objective function 

def objective_rule(model_player):
    return model_player.demand

model_player.value =  Objective( rule=objective_rule, sense=maximize )

#Define revenue constraint 

def revenue_rule(model_player):
    return model_player.price * model_player.demand  <= model_player.revenue 


model_player.revenue_const = Constraint(rule=revenue_rule)

#define data

data = {None: {
    'revenue': {None:8},
    'price': {None:5},
}}

#Example on an instance 

instance = model_player.create_instance(data)
instance.pprint()


results = SolverFactory('glpk').solve(instance)
results.write()
if results.solver.status:
    instance.pprint()