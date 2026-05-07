import re


class player:

    def __init__(self, number: int):
        self.name = "player_" + str(number)
        self.program = {
            "d1": 0,
            "lambda_f": 0,
            "r": 0,
            "revenue": 0,
            "max_demand": 0,
            "sum_demand_type_1": 0,
            "sum_demand_type_2": 0,
            "quantity_given_aggregator": 0,
        }

    def display_variables(self):
        print(self.program)

    def display_agent_programs(self):
        print("Agent name: ", self.name)
        print("Agent program: ")
        print("max d1")
        print("subject to: ", "lambda_f1 * d1 <= " + str(self.program["revenue"]))
        print("d1 <= " + str(self.program["max_demand"]))
