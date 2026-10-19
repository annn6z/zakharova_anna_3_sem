import sys 
import math 
def get_coeff(name):
    while True:
        try:
            return float(input(f"Enter coeff {name}: "))
        except ValueError:
            print("Error: please write correct coeff")
def solution(a,b,c):
    d = b**2 - 4*a*c
    if d<0:
        return []
    t_roots = []
    if d == 0:
        t_roots.append((-b)/2*a)
    else:
        t_roots.append((-b + math.sqrt(d))/2*a)
        t_roots.append((-b - math.sqrt(d))/2*a)
    x_roots = set()
    for t in t_roots:
        if t >= 0:
            x_roots.add(math.sqrt(t))
            x_roots.add(-math.sqrt(t))
    return sorted(list(x_roots))
a = get_coeff ("A")
b = get_coeff ("B")
c = get_coeff ("C")
if a == 0:
    print("A can't be 0")
else:
    result = solution(a,b,c)
    print(f"roots : {result}")
    