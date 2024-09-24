from ortools.sat.python import cp_model
#Used online sources as a reference here along with the professor provided code
# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

## frquencies: (0: f1, 1: f2, 2: f3 )
frequencies = {0: 'f1', 1: 'f2', 2: 'f3'}

# Creating the 9 antennae
Antenna1 = model.NewIntVar(0, 2, 'Antenna 1')
Antenna2 = model.NewIntVar(0, 2, 'Antenna 2')
Antenna3 = model.NewIntVar(0, 2, 'Antenna 3')
Antenna4 = model.NewIntVar(0, 2, 'Antenna 4')
Antenna5 = model.NewIntVar(0, 2, 'Antenna 5')
Antenna6 = model.NewIntVar(0, 2, 'Antenna 6')
Antenna7 = model.NewIntVar(0, 2, 'Antenna 7')
Antenna8 = model.NewIntVar(0, 2, 'Antenna 8')
Antenna9 = model.NewIntVar(0, 2, 'Antenna 9')

# Adding constraints
model.Add(Antenna1 != Antenna2)
model.Add(Antenna1 != Antenna3)
model.Add(Antenna1 != Antenna4)

model.Add(Antenna2 != Antenna1)
model.Add(Antenna2 != Antenna3)
model.Add(Antenna2 != Antenna5)
model.Add(Antenna2 != Antenna6)

model.Add(Antenna3 != Antenna1)
model.Add(Antenna3 != Antenna2)
model.Add(Antenna3 != Antenna6)
model.Add(Antenna3 != Antenna9)

model.Add(Antenna4 != Antenna1)
model.Add(Antenna4 != Antenna2)
model.Add(Antenna4 != Antenna5)

model.Add(Antenna5 != Antenna2)
model.Add(Antenna5 != Antenna4)

model.Add(Antenna6 != Antenna2)
model.Add(Antenna6 != Antenna3)
model.Add(Antenna6 != Antenna7)
model.Add(Antenna6 != Antenna8)

model.Add(Antenna7 != Antenna6)
model.Add(Antenna7 != Antenna8)

model.Add(Antenna8 != Antenna7)
model.Add(Antenna8 != Antenna9)

model.Add(Antenna9 != Antenna3)
model.Add(Antenna9 != Antenna8)

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"Antenna 1: {frequencies[solver.Value(Antenna1)]}")
    print(f"Antenna 2: {frequencies[solver.Value(Antenna2)]}")
    print(f"Antenna 3: {frequencies[solver.Value(Antenna3)]}")
    print(f"Antenna 4: {frequencies[solver.Value(Antenna4)]}")
    print(f"Antenna 5: {frequencies[solver.Value(Antenna5)]}")
    print(f"Antenna 6: {frequencies[solver.Value(Antenna6)]}")
    print(f"Antenna 7: {frequencies[solver.Value(Antenna7)]}")
    print(f"Antenna 8: {frequencies[solver.Value(Antenna8)]}")
    print(f"Antenna 9: {frequencies[solver.Value(Antenna9)]}")
else:
    print("No solution found.")

