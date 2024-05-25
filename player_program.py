from pyomo.environ import *

# create a model
model = ConcreteModel()

# declare decision variables
model.demand = Var(domain=NonNegativeReals)
model.time = Var(domain = NonNegativeReals)

# declare objective
model.profit = Objective(expr = model.demand, sense=maximize)

# declare constraints
model.demand = Constraint(expr = model.demand <= 40)
model.time = Constraint(expr = model.time <= 10 )

# solve
results = SolverFactory('glpk').solve(model)
results.write()
if results.solver.status:
    model.pprint()

# display solution

print('\nDecision Variables')
print('\n Demand = ', model.demand())


print('\nConstraints')
