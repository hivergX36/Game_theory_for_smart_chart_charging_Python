import re 


class player: 
    
    def __init__(self,number) -> None:
        self.name = "player_" + str(number)
        self.program = {
            "a1x^2": 0,
            "b1x": 0,
            "c1": 0,
            "a2x^2": 0,
            "b2x": 0,
            "c2": 0,
            
        }

    def display_program(self):
        return self.program