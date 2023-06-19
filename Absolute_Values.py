from sympy import *
import matplotlib.pyplot as plt
from Mobius_Matrix import input, triangular_numbers, Mobius_Matrix

input()
triangular_numbers()
Mobius_Matrix()

M = Mobius_Matrix(triangular_numbers)
N = M[0, :].tolist()

def abs_value(lst):
    abs_list = [abs(l) for l in lst]
    return abs_list


S = abs_value(N[0])
print(S)
plt.plot(S)
plt.show