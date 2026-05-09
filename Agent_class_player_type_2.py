import re


class player_type_2:

    def __init__(self, number: int):
        self.name = "player_" + str(number)
        self.variables = {
            "d1": 0,
            "lambda_p": 0,
            "r": 0,
            "Q": 0,
            "revenue": 0,
            "max_demand": 0,
            "d_type_1": [0 for i in range(number)],
            "sum_demand_type_1": 0,
            "d_type_2": [0 for i in range(number)],
            "sum_demand_type_2": 0,
            "quantity_given_aggregator": 0,
            "t": 1,
            "type": 2,
        }
        self.instance = {}

    def display_variables(self):
        print(self.variables)

    def display_agent_programs(self):
        print("Agent name: ", self.name)
        print("Agent program: ")
        print("Agent type: ", self.variables["type"])
        print("max d1")
        print("subject to: ", "lambda_f1 * d1 <= " + str(self.variables["revenue"]))
        print("d1 <= " + str(self.variables["max_demand"]))
        if self.variables["type"] == 1:
            print("sum_demand_type_1 + 1/t <= " + "Q")
        else:
            print("sum_demand_type_1 + sum_demand_type_2 + 1/t <= " + "Q")

    def make_instance(self):
        self.instance = {
            self.name: {
                "r": {None: self.variables["r"]},
                "lambda_p": {None: self.variables["lambda_p"]},
                "Q": {None: self.variables["Q"]},
                "r ": {None: self.variables["r"]},
                "d_type_1": {
                    i: self.variables["d_type_1"][i]
                    for i in range(len(self.variables["d_type_1"]))
                },
                "sum_demand_type_1": {None: self.variables["sum_demand_type_1"]},
                "d_type_2": {
                    i: self.variables["d_type_2"][i]
                    for i in range(len(self.variables["d_type_2"]))
                },
                "sum_demand_type_2": {None: self.variables["sum_demand_type_2"]},
            }
        }

    def print_instance(self):
        print(self.instance)
