from pyomo.environ import *


class Aggregator_abstract_model:

    def __init__(self):
        self.aggregator_model = AbstractModel()
        self.aggregator_model.Q1 = Var(within=PositiveReals)
        self.aggregator_model.Q2 = Var(within=PositiveReals)
        self.aggregator_model.price_1 = Param(within=PositiveReals)
        self.aggregator_model.price_2 = Param(within=PositiveReals)
        self.aggregator_model.Min_Q = Param(within=PositiveReals)
        self.aggregator_model.Max_Q = Param(within=PositiveReals)
        self.aggregator_model.Sum_demand = Param(within=PositiveReals)
        self.aggregator_model.Sum_demand_type_1 = Param(within=PositiveReals)
        self.aggregator_model.Sum_demand_type_2 = Param(within=PositiveReals)

        # define objective function

        def objective_rule(aggregator_model):
            return (
                aggregator_model.Q1
                + aggregator_model.Q2
                + aggregator_model.price_1
                * (aggregator_model.Q1 - aggregator_model.Sum_demand_type_1)
                + aggregator_model.price_2
                * (aggregator_model.Q2 - aggregator_model.Sum_demand_type_2)
            )

        self.aggregator_model.objective = Objective(rule=objective_rule, sense=minimize)

        # Define quantity sup

        def constraint_sup_quantity_rule(aggregator_model):
            return aggregator_model.Q1 + aggregator_model.Q2 <= aggregator_model.Max_Q

        self.aggregator_model.constraint_debit = Constraint(
            rule=constraint_sup_quantity_rule
        )

        def constraint_inf_quantity_rule(aggregator_model):
            return aggregator_model.Q1 + aggregator_model.Q2 >= aggregator_model.Min_Q

        self.aggregator_model.constraint_inf_quantity = Constraint(
            rule=constraint_inf_quantity_rule
        )

        def constraint_priority_demand(aggregator_model):
            return aggregator_model.Q1 + aggregator_model.Sum_demand_type_1 >= sum(
                aggregator_model.Q2 - aggregator_model.Sum_demand_type_2
            )

        self.aggregator_model.constraint_priority_demand = Constraint(
            rule=constraint_priority_demand
        )
