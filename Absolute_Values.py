from sympy import *
import matplotlib.pyplot as plt
from mobius_matrix import triangular_numbers, mobius_matrix

M = mobius_matrix(triangular_numbers())
N = M[0, :].tolist()

def abs_value(lst):
    abs_list = [abs(l) for l in lst]
    return abs_list


S = abs_value(N[0])
plt.plot(S)
plt.show()