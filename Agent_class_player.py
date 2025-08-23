import re 


class player: 
    
    def __init__(self,number, r, time, demand) -> None:
        self.name = "player_" + str(number)
        self.revenu = r
        self.time = time
        self.demand = demand
        self.instance = {}
        
    def rename(self, new_name):
        self.name = new_name
        
    def define_revenu(self, new_revenu):
        self.revenu = new_revenu 
        
    def define_time(self,new_time):
        self.time = new_time

    def define_demand(self, new_demand):
        self.demand = new_demand