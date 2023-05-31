from sympy import *
import matplotlib.pyplot as plt
import numpy as np

number = int(input("Number: "))
triangular_numbers = ([(x * (x + 1) // 2) for x in range(1, number+1)])
def Mobius_Matrix(lst):
    zeta_array = [[0 if n % m != 0 else 1 for n in lst] for m in lst]
    return Matrix(zeta_array) ** -1
M = Mobius_Matrix(triangular_numbers)
N = M[0, :].tolist()


def abs_value(lst):
    abs_list = [abs(l) for l in lst]
    return abs_list

def sum_function(abs_list):
    sum_list = [sum(abs_list[:i+1]) for i in range(len(abs_list))]
    return sum_list

S = sum_function(abs_value(N[0]))
slope = (S[-1] - S[0])/(number - 0)
print(slope)
plt.plot(S)
plt.show
#slope approaching 0.5