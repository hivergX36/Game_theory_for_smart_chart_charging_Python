from pyomo.environ import *

# create a model
model = ConcreteModel()

# declare decision variables
model.quantity = Var(domain=NonNegativeReals)

# declare objective
model.cost = Objective(expr = model.quantity, sense=minimize)

# declare constraints
# On peut faire un Set 

model.constraint_quantity_1 = Constraint(expr = model.quantity <= 40)
model.constraint_quantity_2 = Constraint(expr = model.quantity >= 10)

# solve
results = SolverFactory('glpk').solve(model)
results.write()
if results.solver.status:
    model.pprint()

# display solution

print('\nDecision Variables')
print('\n quanity = ', model.quantity())


print('\nConstraints')
print('constraint_quantity_1  = ', model.constraint_quantity_1())
print('constraint_quantity_2  = ', model.constraint_quantity_2())

