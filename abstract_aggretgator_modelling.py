from pyomo.environ import *

model_aggregator = AbstractModel() 

model_aggregator.quantity = Var(within = PositiveReals)
model_aggregator.min_quantity = Param(within = PositiveReals)
model_aggregator.max_quantity = Param(within = PositiveReals)
model_aggregator_agent_demand_set = Set()

#define objective function 

def objective_rule(model_player):
    return model_aggregator.quantity

model_aggregator.value =  Objective( rule=objective_rule, sense=minimize)

#Define revenue constraint 

def constraint_sup_quantity_rule(model_aggregator):
    return model_aggregator.quantity  <= model_aggregator.max_quantity


def constraint_inf_quantity_rule(model_aggregator):
    return model_aggregator.quantity  >= model_aggregator.min_quantity


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