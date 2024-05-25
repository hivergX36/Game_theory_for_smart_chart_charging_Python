from pyomo.environ import *
# build abstact model
model       = AbstractModel()
 
# define abstract parameters
model.ITEMS = Set()
model.v     = Param( model.ITEMS, within=PositiveReals )
model.w     = Param( model.ITEMS, within=PositiveReals )
model.W_max = Param( within=PositiveReals )
model.x     = Var( model.ITEMS, within=Binary )
 
# defind objective function
def value_rule(model):
    return sum( model.v[i]*model.x[i] for i in model.ITEMS )
model.value = Objective( rule=value_rule, sense=maximize )
 
# define constraint
def weight_rule(model):
    return sum( model.w[i]*model.x[i] for i in model.ITEMS ) <= model.W_max
model.weight = Constraint( rule=weight_rule)

# define data

data = {None: {
    'ITEMS': {None: ["hammer","wrench"]},
    'v': {"hammer":8, "wrench":3},
    'w': {"hammer": 10, "wrench":7},
    'W_max': {None:24},
}}
i = model.create_instance(data)
i.pprint()

#solve the model 

results = SolverFactory('glpk').solve(i)
results.write()
if results.solver.status:
    i.pprint()

# display solution

print('\n hammer = ', i.x["hammer"]())
print('\n wrench = ', i.x["wrench"]())

#Another instance 
data2 = {None: {
    'ITEMS': {None: ["hammer","wrench"]},
    'v': {"hammer":8, "wrench":3},
    'w': {"hammer": 10, "wrench":7},
    'W_max': {None:10},
}}


i = model.create_instance(data2)
i.pprint()

results = SolverFactory('glpk').solve(i)
results.write()
if results.solver.status:
    i.pprint()
