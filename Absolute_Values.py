from sympy import *
import matplotlib.pyplot as plt
from mobius_matrix import triangular_numbers, mobius_matrix

number = int(input("Number: "))

M = mobius_matrix(number)
N = M[0, :].tolist()


def abs_value(lst):
    abs_list = [abs(l) for l in lst]
    return abs_list


lst = N[0]
S = abs_value(lst)
plt.plot(S)
plt.show()
