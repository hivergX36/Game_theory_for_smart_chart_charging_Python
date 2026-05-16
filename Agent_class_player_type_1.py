import re


class player_type_1:

    def __init__(self, number: int, number_of_agent_type_1: int):
        self.name = "player_" + str(number)
        self.variables = {
            "d": 0,
            "r": 0,
            "Q1": 0,
            "Q2": 0,
            "Q": 0,
            "lambda_price_1": 0,
            "max_demand": 0,
            "d_type_1": [0 for i in range(number_of_agent_type_1)],
            "sum_another_demand_type_1": 0,
            "waiting_price": 0,
            "t": 1,
            "type": 1,
        }
        self.instance = {}

    def display_variables(self):
        print(self.variables)

    def display_agent_programs(self):
        print("Agent name: ", self.name)
        print("Agent program: ")
        print("Agent type: ", self.variables["type"])
        print("max d")
        print("subject to: ", "lambda_f1 * d <= " + str(self.variables["r"]))
        print("d <= " + str(self.variables["max_demand"]))
        if self.variables["type"] == 1:
            print("sum_another_demand_type_1 + 1/t <= " + "Q")
        else:
            print("sum_another_demand_type_1 +sum_demand_type_2 + 1/t <= " + "Q")

    def make_instance(self):
        self.instance = {
            None: {
                "r": {None: self.variables["r"]},
                "lambda_price_1": {None: self.variables["lambda_price_1"]},
                "Q": {None: self.variables["Q"]},
                "Q1": {None: self.variables["Q1"]},
                "Q2": {None: self.variables["Q2"]},
                "r ": {None: self.variables["r"]},
                "t": {None: self.variables["t"]},
                "max_demand": {None: self.variables["max_demand"]},
                "waiting_price": {None: self.variables["waiting_price"]},
                "d_type_1": {
                    i: self.variables["d_type_1"][i]
                    for i in range(len(self.variables["d_type_1"]))
                },
                "sum_another_demand_type_1": {
                    None: self.variables["sum_another_demand_type_1"]
                },
            }
        }

    def print_instance(self):
        print(self.instance)

    def dislay_solution(self):
        print("Results for ", self.name, ":")
        print("d: ", self.variables["d"])
        print("lambda_price_1: ", self.variables["lambda_price_1"])
