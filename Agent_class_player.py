import re 


class player: 
    
    def __init__(self, number: int) -> None:
        self.name = "player_" + str(number)
        self.program = {
            "d1": 0,
            "lambda_f": 0,
            "r": 0,
            "revenue": 0,
            "min_demand": 0,
            "max_demand": 0,
            "sum_demand": 0,
            "quantity": 0,
            'sum_another_demand': 0
            
        }

    def display_program(self):
        print(self.program)
        
