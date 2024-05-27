import re 


class player: 
    
    def __init__(self,number) -> None:
        self.name = "player_" + str(number)
        self.revenu = 0 
        self.time = 0 
        self.demand = 0 
        self.instance = {}
        
    def rename(self, new_name):
        self.name = new_name
        
    def define_revenu(self, new_revenu):
        self.revenu = new_revenu 
        
    def define_time(self,new_time):
        self.time = new_time
        
class aggregator:
    
    def __init__(self) -> None:
        self.quantity_distributed = 0 
        self.Qmax = 0 
        self.Qmin = 0 
        self.price = 0
        self.instance = {} 
        
    def define_quantity(self,new_quantity):
        self.quantity_distributed = new_quantity 
    
    def define_max_quantity(self, new_max):
        self.Qmax = new_max 
        
    def definie_min_quantity(self, new_min):
        self.Qmin = new_min 
        
    def definie_price(self, shadow_price):
        self.price = shadow_price
        

class controler:
    
    def __init__(self) -> None:
        self.aggregator_price = 0
        self.aggregator_quantity = []
        self.time_list = []
        self.player_type_list = []
        self.revenu_list = []
        self.nb_player = 0 
        self.nb_aggregator = 0 
                
        
    def checknumber(self,lignes,indice):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != "," and lignes[indice][compteur2] != ","):
              while(lignes[indice][compteur2] != ","):
                    compteur2 += 1
              print(lignes[indice][compteur1:compteur2])
              ParsedList.append(int(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1

   
              if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
        
    def read_data(self,text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [ re.sub("\n", "", lines[i]) for i in range(len(lines))]
        print("lines: ", lines)
        self.aggregator_price = self.checknumber(lines,1)[0]
        print("price: ", self.aggregator_price)
        self.time_list = self.checknumber(lines,3)
        print("time_list", self.time_list)
        self.revenu_list = self.checknumber(lines,5)
        print("revenu_list", self.revenu_list)
        self.quantity_list = self.checknumber(lines,7)
        print (self.quantity_list)
        self.nb_player = len(self.revenu_list)
        
    def return_agent_data(self,players:list[player],aggregator:aggregator):
        length = len(players)
        aggregator.price = self.aggregator_price
        aggregator.Qmin = self.aggregator_quantity[0]
        aggregator.Qmax = self.aggregator_quantity[1]
        data_aggregator = {None: {'min_quantity': {None:1},'max_quantity': {None:100},'agent_demand_set':{None:[i for i in range(length)]},'agent_demand':{1:10,2:9,3:15},
}}
        for i in range(length):
            players[i].time = self.time_list[i]
            players[i].revenu = self.revenu_list[i]
            players[i].instance  = {None: {'revenue': {None:self.revenu_list[i]},'price': {None:self.aggregator_price}}}

        
     
    
    def return_aggregator_solution(self,aggregator:aggregator, quantity): 
        aggregator.quantity_distributed = quantity 
        
    def return_player_solution(self,players:list[player],demand,compteur):
        players[compteur].demand = demand        
        