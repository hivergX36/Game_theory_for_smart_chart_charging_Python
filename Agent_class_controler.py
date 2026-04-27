import re
from Agent_class_player import player
from Agent_class_aggregator import aggregator


class controler:

    def __init__(self, number_of_agent: int) -> None:
        self.agent_list = [player(i) for i in range(number_of_agent)]
        self.aggregator = aggregator()

    def read_data_player(self, text: str):
        index_word = 0
        dictionnary_word = ["d1", "lambda_f", "r", "revenue", "min_demand", "max_demand", "sum_demand", "quantity", 'sum_another_demand']
        fichier = open(text, "r", encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [re.sub("\n", "", lines[i]) for i in range(len(lines))]
        lines = [re.sub(":", "", lines[i]) for i in range(len(lines))]
        print(lines)
        for w in dictionnary_word:
            for i in range(len(lines)):
                if w in lines[i]:
                    parsed_lines = [float(s) for s in lines[i + 1].split(",")]
                    for index_float in range(len(parsed_lines)):
                        self.agent_list[index_float].program[w] = float(
                            parsed_lines[index_float]
                        )
        print("lines: ", lines)

    def read_data_aggregator(self, text: str):
        index_word = 0
        dictionnary_word = [ "d1", "lambda_f", "r", "revenue", "min_demand", "max_demand", "sum_demand", "quantity", 'sum_another_demand']
        fichier = open(text, "r", encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [re.sub("\n", "", lines[i]) for i in range(len(lines))]
        lines = [re.sub(":", "", lines[i]) for i in range(len(lines))]
        for w in dictionnary_word:
            for i in range(len(lines)):
                if w in lines[i]:
                    parsed_lines = [float(s) for s in lines[i + 1].split(",")]
                    for index_float in range(len(parsed_lines)):
                        self.aggregator.instance[w] = float(parsed_lines[index_float])
        print("lines: ", lines)

    def print_controler(self):
        for agent in self.agent_list:
            print("Agent Name: ", agent.name)
            print("Agent Program: ", agent.program)
            print("-----------------------")
        print("Aggregator Instance: ", self.aggregator.instance)
