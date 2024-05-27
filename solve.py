from pyomo.environ import *
from Abstract_aggretgator_modelling import *
from Abstract_player_modelling import *


#define data

data_player = {None: {
    'revenue': {None:8},
    'price': {None:5},
}}

#Example on a player instance 

instance_player = model_player.create_instance(data_player)
instance_player.pprint()


results_player = SolverFactory('glpk').solve(instance_player)
results_player.write()
if results_player.solver.status:
    instance_player.pprint()
    
#define data

data_aggregator = {None: {
    'min_quantity': {None:1},
    'max_quantity': {None:100},
    'agent_demand_set':{None:[1,2,3]},
    'agent_demand':{1:10,2:9,3:15},
}}

#Example on an instance 

instance_aggregator = model_aggregator.create_instance(data_aggregator)
instance_aggregator.pprint()


results_aggregator = SolverFactory('glpk').solve(instance_aggregator)