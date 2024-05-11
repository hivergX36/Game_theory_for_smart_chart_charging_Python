from Agent import agent

class aggregator:
    
    def __init__(self) -> None:
        self.quantity_distributed = 0 
        self.Qmax = 0 
        self.Qmin = 0 
        self.price = 0 
        
    def define_quantity(self,new_quantity):
        self.quantity_distributed = new_quantity 
    
    def define_max_quantity(self, new_max):
        self.Qmax = new_max 
        
    def definie_min_quantity(self, new_min):
        self.Qmin = new_min 
        
    def definie_price(self, shadow_price):
        self.price = shadow_price
        
