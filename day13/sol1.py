from ortools.linear_solver import pywraplp
PART2 = True
tokens = 0
                    
with open("input13.txt", 'r') as f:
    lines = [line.strip() for line in f if line.strip()]  
    num_lines = len(lines)
    ptr = 0


    while True:

        if ptr > (num_lines - 3):
            break

        line_a = lines[ptr]
        line_b = lines[ptr+1]
        line_prize = lines[ptr+2]

        _, coords_a = line_a.split(": ")
        x_a_str, y_a_str = coords_a.split(", ")
        x_a = int(x_a_str.replace("X+", ""))
        y_a = int(y_a_str.replace("Y+", ""))

        _, coords_b = line_b.split(": ")
        x_b_str, y_b_str = coords_b.split(", ")
        x_b = int(x_b_str.replace("X+", ""))
        y_b = int(y_b_str.replace("Y+", ""))

        _, coords_prize = line_prize.split(": ")
        x_p_str, y_p_str = coords_prize.split(", ")
        x_p = int(x_p_str.replace("X=", ""))+PART2*10000000000000
        y_p = int(y_p_str.replace("Y=", ""))+PART2*10000000000000




        # Do the solve
        solver = pywraplp.Solver.CreateSolver('SCIP')

        A = solver.IntVar(0, solver.infinity(), 'A')
        B = solver.IntVar(0, solver.infinity(), 'B')
        
        print(f"Equation is A*{x_a} , B*{x_b} = {x_p}")
        constraint1 = solver.Add(x_a * A + x_b * B == x_p)
        print(f"Equation is A*{y_a} + B*{y_b} = {y_p}")
        constraint2 = solver.Add(y_a * A + y_b * B == y_p)
        print(F"Minimize C = 3A + B")
        solver.Minimize(3 * A + B)

        status = solver.Solve()

        if status == solver.OPTIMAL:
            A = A.solution_value()
            B = B.solution_value()
            assert A >= 0
            assert B >= 0
            C = 3*A + B
            assert C > 0
            print('Solution:')
            print(f"{A,B,C}")
            tokens += C
        else:
            print('The solver did not find an optimal solution.')
        
        ptr +=3
        
print(tokens)