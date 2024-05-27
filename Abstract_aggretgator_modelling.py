from pyomo.environ import *

model_aggregator = AbstractModel() 

model_aggregator.quantity = Var(within = PositiveReals)
model_aggregator.min_quantity = Param(within = PositiveReals)
model_aggregator.max_quantity = Param(within = PositiveReals)
model_aggregator.agent_demand_set = Set()
model_aggregator.agent_demand = Param(model_aggregator.agent_demand_set, within = PositiveReals)
#define objective function 

def objective_rule(model_aggregator):
    return model_aggregator.quantity

model_aggregator.value =  Objective( rule=objective_rule, sense=minimize)

#Define revenue constraint 

def constraint_sup_quantity_rule(model_aggregator):
    return model_aggregator.quantity  <= model_aggregator.max_quantity

model_aggregator.constraint_sup_quantity = Constraint(rule = constraint_sup_quantity_rule)


def constraint_inf_quantity_rule(model_aggregator):
    return model_aggregator.quantity  >= model_aggregator.min_quantity

model_aggregator.constraint_inf_quantity = Constraint(rule = constraint_inf_quantity_rule)

def constraint_demand_quantity_rule(model_aggregator):
    return model_aggregator.quantity >= sum(model_aggregator.agent_demand[i] for i in model_aggregator.agent_demand_set) 

model_aggregator.constraint_quantity_distributed = Constraint(rule = constraint_demand_quantity_rule)


