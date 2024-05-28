from pyomo.environ import * 
from Agent import *
from Abstract_player_modelling import *
from Abstract_aggretgator_modelling import *

joueur = [player(i) for i in range(10)]
aggregateur = aggregator()
controleur = controler()

controleur.read_data("data.txt")
controleur.return_agent_data(joueur,aggregateur)
print(aggregateur.instance)
print(joueur[3].instance)

for i in range(10):
    instance_player = model_player.create_instance(joueur[i].instance)
    results_player = SolverFactory('glpk').solve(instance_player)
    results_player.write()
    if results_player.solver.status:
        instance_player.pprint()
    joueur[i].demand = value(instance_player.demand)
    

print(type(joueur[3].demand))
print(joueur[7].demand)

controleur.modify_aggregator_instances(joueur,aggregateur)

instance_aggregator = model_aggregator.create_instance(aggregateur.instance)
results_aggregator = SolverFactory('glpk').solve(instance_aggregator)
if results_aggregator.solver.status:
    instance_aggregator.pprint()
    