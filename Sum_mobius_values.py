from sympy import *
import matplotlib.pyplot as plt
from Mobius_Matrix import Mobius_Matrix, triangular_numbers


M = Mobius_Matrix(triangular_numbers())
N = M[0, :].tolist()

def sum_function(lst):
    sum_list = [sum(lst[:i+1]) for i in range(len(lst))]
    return sum_list

S = sum_function(N[0])
plt.plot(S)
plt.show()