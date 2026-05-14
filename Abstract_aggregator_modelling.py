from pyomo.environ import *


class Aggregator_abstract_model:

    def __init__(self):
        self.model = AbstractModel()
        self.Q1_solution = 0
        self.Q2_solution = 0
        self.model.Q1 = 0
        self.model.Q2 = 0
        self.model.Q1 = Var(within=NonNegativeReals)
        self.model.Q2 = Var(within=NonNegativeReals)
        self.model.price_1 = Param(within=NonNegativeReals)
        self.model.price_2 = Param(within=NonNegativeReals)
        self.model.Min_Q = Param(within=NonNegativeReals)
        self.model.Max_Q = Param(within=NonNegativeReals)
        self.model.Sum_demand = Param(within=NonNegativeReals)
        self.model.Sum_demand_type_1 = Param(within=NonNegativeReals)
        self.model.Sum_demand_type_2 = Param(within=NonNegativeReals)

        # define objective function

        def objective_rule(model):
            return (
                model.Q1
                + model.Q2
                + model.price_1 * (model.Sum_demand_type_1 - model.Q1)
                + model.price_2 * (model.Sum_demand_type_2 - model.Q2)
            )

        self.model.objective = Objective(rule=objective_rule, sense=minimize)

        # Define quantity sup

        def constraint_sup_quantity_rule(model):
            return model.Q1 + model.Q2 <= model.Max_Q

        self.model.constraint_debit = Constraint(rule=constraint_sup_quantity_rule)

        def constraint_inf_quantity_rule(model):
            return model.Q1 + model.Q2 >= model.Min_Q

        self.model.constraint_inf_quantity = Constraint(
            rule=constraint_inf_quantity_rule
        )

        def constraint_priority_demand(model):
            return (
                model.Q1 - model.Sum_demand_type_1 >= model.Q2 - model.Sum_demand_type_2
            )

        self.model.constraint_priority_demand = Constraint(
            rule=constraint_priority_demand
        )

    def run_model(self, data):
        instance = self.model.create_instance(data)
        instance.pprint()
        # Solver setup (GLPK is used here)
        solver = SolverFactory("glpk")
        # Solve the model
        solver.solve(instance)
        print("Results for Aggregator:")
        instance.Q1.pprint()
        instance.Q2.pprint()
        self.Q1_solution = instance.Q1.value
        self.Q2_solution = instance.Q2.value
