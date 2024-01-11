from sympy import *
import matplotlib.pyplot as plt
from mobius_matrix import mobius_matrix, triangular_numbers


number = int(input("Number: "))

M = mobius_matrix(triangular_numbers(number))
N = M[0, :].tolist()

def sum_function(lst):
    sum_list = [sum(lst[:i+1]) for i in range(len(lst))]
    return sum_list

S = sum_function(N[0])
plt.plot(S)
plt.show()