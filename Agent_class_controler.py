import re
from Agent_class_player_type_1 import player_type_1
from Agent_class_player_type_2 import player_type_2
from Agent_class_aggregator import aggregator


class controler:

    def __init__(self, number_of_agent_type_1: int, number_of_agent_type_2: int):
        self.agent_list_type_1 = [
            player_type_1(i) for i in range(number_of_agent_type_1)
        ]
        self.agent_list_type_2 = [
            player_type_2(i) for i in range(number_of_agent_type_2)
        ]
        self.aggregator = aggregator()

    def read_data_player_type_1(self, text: str):
        index_word = 0
        dictionnary_word = [
            "d1",
            "lambda_f",
            "r",
            "max_demand",
            "sum_demand_type_1",
            "Q",
            "t",
        ]
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
                        self.agent_list_type_1[index_float].variables[w] = float(
                            parsed_lines[index_float]
                        )
        print("lines: ", lines)

    def read_data_player_type_2(self, text: str):
        index_word = 0
        dictionnary_word = [
            "d1",
            "lambda_f",
            "r",
            "revenue",
            "max_demand",
            "sum_demand_type_1",
            "sum_demand_type_2",
            "Q",
            "t",
        ]
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
                        self.agent_list_type_2[index_float].variables[w] = float(
                            parsed_lines[index_float]
                        )
        print("lines: ", lines)

    def read_data_aggregator(self, text: str):
        index_word = 0
        dictionnary_word = [
            "Max_Q",
            "Min_Q",
            "lambda_f",
            "revenue",
            "sum_demand",
            "Q",
        ]
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
        for agent in self.agent_list_type_1:
            print("Agent Name: ", agent.name)
            print("Agent variables: ", agent.display_variables())
            print("Agent Program: ", agent.display_agent_programs())
            print("-----------------------")
        for agent in self.agent_list_type_2:
            print("Agent Name: ", agent.name)
            print("Agent variables: ", agent.display_variables())
            print("Agent Program: ", agent.display_agent_programs())
            print("-----------------------")
        print("Aggregator variables: ", self.aggregator.display_aggregator_variables())
        print("-----------------------")
        print("Aggregator programs: ", self.aggregator.display_aggregator_programs())

    def make_instance(self):
        for agent in self.agent_list_type_1:
            agent.make_instance()
        for agent in self.agent_list_type_2:
            agent.make_instance()
        self.aggregator.make_instance()

    def print_instance(self):
        for agent in self.agent_list_type_1:
            print("Agent Name: ", agent.name)
            print("Agent instance: ", agent.print_instance())
            print("-----------------------")
        for agent in self.agent_list_type_2:
            print("Agent Name: ", agent.name)
            print("Agent instance: ", agent.print_instance())
            print("-----------------------")
        print("Aggregator instance: ", self.aggregator.print_instance())
