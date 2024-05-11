
class player: 
    
    def __init__(self,number) -> None:
        self.name = "player_" + str(number)
        self.revenu = 0 
        self.time = 0 
        
    def rename(self, new_name):
        self.name = new_name
        
    def define_revenu(self, new_revenu):
        self.revenu = new_revenu 
        
    def define_time(self,new_time):
        self.time = new_time
        
        
        