import sys
import math

class BiquadraticEquation:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.roots = []

    def get_coefficient(self, index, name):
        # Check command line arguments first
        if len(sys.argv) > index:
            try:
                return float(sys.argv[index])
            except ValueError:
                print(f"Argument {name} from command line is invalid.")
        
        # Interactive keyboard input loop
        while True:
            try:
                return float(input(f"Enter coefficient {name}: "))
            except ValueError:
                print("Error: Please enter a valid number.")

    def load_coefficients(self):
        self.a = self.get_coefficient(1, "A")
        self.b = self.get_coefficient(2, "B")
        self.c = self.get_coefficient(3, "C")

    def solve(self):
        d = self.b**2 - 4 * self.a * self.c
        if d < 0:
            self.roots = []
            return
            
        t_roots = []
        if d == 0:
            t_roots.append(-self.b / (2 * self.a))
        else:
            t_roots.append((-self.b + math.sqrt(d)) / (2 * self.a))
            t_roots.append((-self.b - math.sqrt(d)) / (2 * self.a))

        # Find x roots from t roots using .add() for set
        x_roots = set()
        for t in t_roots:
            if t >= 0:
                x_roots.add(math.sqrt(t))
                x_roots.add(-math.sqrt(t))
        self.roots = sorted(list(x_roots))

    def print_result(self):
        if self.a == 0:
            print("Coefficient A cannot be zero!")
        elif not self.roots:
            print("No real roots found.")
        else:
            print(f"Real roots: {self.roots}")


if __name__ == "__main__":
    
    equation = BiquadraticEquation()
    equation.load_coefficients()
    equation.solve()
    equation.print_result()
