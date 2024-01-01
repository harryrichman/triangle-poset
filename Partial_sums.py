from sympy import *
import matplotlib.pyplot as plt
from mobius_matrix import mobius_matrix, triangular_numbers


M = mobius_matrix(triangular_numbers())
N = M[0, :].tolist()

def partial_sums(lst):
    result = [sum(lst[:i+1]) for i in range(len(lst))]
    return result

S = partial_sums(N[0])
plt.plot(S)
plt.show()