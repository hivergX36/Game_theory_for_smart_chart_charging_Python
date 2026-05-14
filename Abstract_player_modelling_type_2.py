from pyomo.environ import *


class Player_abstract_model_type_2:

    def __init__(self):
        self.player_solution = 0
        self.model = AbstractModel()
        self.model.lambda_p = Param(within=NonNegativeReals)
        self.model.r = Param(within=NonNegativeReals)
        self.model.Q = Param(within=NonNegativeReals)
        self.model.sum_another_demand_type_1 = Param(within=NonNegativeReals)
        self.model.sum_another_demand_type_2 = Param(within=NonNegativeReals)
        self.model.t = Param(within=NonNegativeReals)
        self.model.max_demand = Param(within=NonNegativeReals)
        self.model.waiting_price = Param(within=NonNegativeReals)

        # Define the decision variables for demand, indexed by players
        self.model.d1 = Var(within=NonNegativeReals)

        # Define the objective: maximize total demand across all players
        def objective_rule(model):
            return model.d1 - model.waiting_price * (
                model.d1
                + model.sum_another_demand_type_1
                + model.sum_another_demand_type_2
                + 1 / model.t
                - model.Q
            )

        self.model.objective = Objective(rule=objective_rule, sense=maximize)

        # Define the revenue constraint: demand * price should be less than or equal to revenue
        def revenue_rule(model, p):
            return model.d1 * model.lambda_p <= model.r

        self.model.revenue_constraint = Constraint(rule=revenue_rule)

        def model_demand_constraint(model):
            return model.d1 <= model.max_demand

        self.model.demand_constraint = Constraint(rule=model_demand_constraint)

    def run_model(self, data):
        instance = self.model.create_instance(data)
        instance.pprint()
        # Solver setup (GLPK is used here)
        solver = SolverFactory("glpk")
        # Solve the model
        solver.solve(instance)
        print("Results for Player 2:")
        instance.d1.pprint()
        self.player_solution = instance.d1.value
