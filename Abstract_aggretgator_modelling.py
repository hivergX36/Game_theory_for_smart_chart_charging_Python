from pyomo.environ import *


class Aggregator_abstract_model:
    
        def __init__(self):
            self.aggregator_model = AbstractModel()
            self.quantity = Var(within = PositiveReals)
            self.min_quantity = Param(within = PositiveReals)
            self.max_quantity = Param(within = PositiveReals)
            self.agent_demand_set = Set()
            self.agent_demand = Param(self.agent_demand_set, within = PositiveReals)
            
            #define objective function 

            def objective_rule(aggregator_model):
                return aggregator_model.quantity

            self.aggregator_model.objective = Objective(rule=objective_rule, sense=minimize)
            
            #Define revenue constraint 

            def constraint_revenue_rule(model_aggregator):
                return model_aggregator.agent_demand[model_aggregator.agent_demand_set] <= model_aggregator.quantity

            self.model_aggregator.constraint_revenue = Constraint(rule=constraint_revenue_rule)


            #Define quantity constraints
            
            def constraint_sup_quantity_rule(model_aggregator):
                return model_aggregator.quantity  <= model_aggregator.max_quantity

            self.model_aggregator.constraint_sup_quantity = Constraint(rule = constraint_sup_quantity_rule)


            def constraint_inf_quantity_rule(model_aggregator):
                return model_aggregator.quantity  >= model_aggregator.min_quantity

            self.model_aggregator.constraint_inf_quantity = Constraint(rule = constraint_inf_quantity_rule)

            def constraint_demand_quantity_rule(model_aggregator):
                return model_aggregator.quantity >= sum(model_aggregator.agent_demand[i] for i in model_aggregator.agent_demand_set) 

            self.model_aggregator.constraint_quantity_distributed = Constraint(rule = constraint_demand_quantity_rule)


