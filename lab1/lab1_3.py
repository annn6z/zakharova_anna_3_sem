import sys
import math

def get_coefficient(index, name):
    if len(sys.argv) > index:
        try:
            return float(sys.argv[index])
        except ValueError:
            print(f"Argument {name} from command line is invalid.")
            
    while True:
        try:
            return float(input(f"Enter coefficient {name}: "))
        except ValueError:
            print("Error: Please enter a valid number.")

def solve_biquadratic(a, b, c):
    d = b**2 - 4*a*c
    
    # Structural Pattern Matching (Python 3.10+)
    match d:
        case _ if d < 0:
            return []  # No roots if discriminant is negative
        case 0.0:
            t_roots = [-b / (2 * a)]
        case _:
            t_roots = [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]

    # Calculate x roots from t
    x_roots = set()
    for t in t_roots:
        if t >= 0:
            x_roots.add(math.sqrt(t))
            x_roots.add(-math.sqrt(t))
            
    return sorted(list(x_roots))

def main():
    
    a = get_coefficient(1, "A")
    b = get_coefficient(2, "B")
    c = get_coefficient(3, "C")

    if a == 0:
        print("Coefficient A cannot be zero!")
    else:
        result = solve_biquadratic(a, b, c)
        if not result:
            print("No real roots found.")
        else:
            print(f"Real roots: {result}")

if __name__ == "__main__":
    main()
