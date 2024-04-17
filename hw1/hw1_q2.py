"""
Homework 1
2 (e) & (f)
"""
    
import numpy as np
from itertools import permutations,product

factorial = np.math.factorial
                
def v_e(x1=0, x2=0, x3=0):  
    return x1 + 2*x2 + 3*x3

def v_f(x1=0, x2=0, x3=0, x4=0, x5=0):  
    return x2+x3+2*x4+3*x1*x3 + 5*x2*x5 - 10*x1*x2*x4

def compute_shapley_value(v, n):
    #n:  Number of players
    shapley_values = np.zeros(n)
    # Get all permutations of three elements where each element is either 0 or 1
    permutations = list(product([0, 1], repeat=n))

    for i in range(n):
            marginals = []

            for p in permutations:
                if p[i] == 1:
                    continue
                value_o_i = v(*p)
                value_w_i = v(*p[:i] + (1,) + p[i+1:])
                marginals.append((value_w_i - value_o_i) * (factorial(n - 1 - sum(p)) * factorial(sum(p))) / factorial(n))

            shapley_values[i] = np.sum(marginals)

    return shapley_values

shapley_values = compute_shapley_value(v_f, 5)
print("Shapley values:", shapley_values)
# Verify the efficiency
print("Sum of Shapley values:", np.sum(shapley_values))
print("Shapley value for all players:", v_f(*[1]*5))
      
