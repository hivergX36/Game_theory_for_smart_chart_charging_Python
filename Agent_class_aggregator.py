class aggregator:
    """_summary_
    This class represents an aggregator in the smart charging system.
    This the pyomo abstract model of the aggregator
    """

    def __init__(self):
        self.instance = {
            "Q": 0,
            "Max_Q": 0,
            "Min_Q": 0,
        }

    def display_aggregator_variables(self):
        print(self.instance)

    def display_aggregator_programs(self):
        print("Aggregator program: ")
        print("min Q")
        print("subject to: ", "Q <= " + str(self.instance["Max_Q"]))
        print("Q >= " + str(self.instance["Min_Q"]))
