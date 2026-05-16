class aggregator:
    """_summary_
    This class represents an aggregator in the smart charging system.
    This the pyomo abstract model of the aggregator
    """

    def __init__(self):
        self.variables = {
            "Q": 0,
            "Max_Q": 0,
            "Min_Q": 0,
            "Sum_demand_type_1": 0,
            "Sum_demand_type_2": 0,
            "Sum_demand": 0,
            "price_1": 0,
            "price_2": 0,
        }
        self.instance = {}

    def display_aggregator_variables(self):
        print(self.instance)

    def display_aggregator_programs(self):
        print("Aggregator program: ")
        print("min Q")
        print("subject to: ", "Q <= " + str(self.instance["Max_Q"]))
        print("Q >= " + str(self.instance["Min_Q"]))

    def get_all_demand(self, agent_list_type_1, agent_list_type_2):
        sum_demand_type_1 = 0
        sum_demand_type_2 = 0
        for agent in agent_list_type_1:
            sum_demand_type_1 += agent.variables["d"]
        for agent in agent_list_type_2:
            sum_demand_type_2 += agent.variables["d"]
        self.variables["Sum_demand_type_1"] = sum_demand_type_1
        self.variables["Sum_demand_type_2"] = sum_demand_type_2
        self.variables["Sum_demand"] = sum_demand_type_1 + sum_demand_type_2

    def make_instance(self):
        self.instance = {
            None: {
                "Q": {None: self.variables["Q"]},
                "Max_Q": {None: 10},
                "Min_Q": {None: self.variables["Min_Q"]},
                "Sum_demand_type_1": {None: self.variables["Sum_demand_type_1"]},
                "Sum_demand_type_2": {None: self.variables["Sum_demand_type_2"]},
                "Sum_demand": {None: self.variables["Sum_demand"]},
                "price_1": {None: self.variables["price_1"]},
                "price_2": {None: self.variables["price_2"]},
            }
        }

    def print_instance(self):
        print(self.instance)

    def dislay_solution(self):
        print("Results for Aggregator ")
        print("Q1: ", self.variables["Q1"])
        print("Q2: ", self.variables["Q2"])
