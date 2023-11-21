from sympy import *
import matplotlib.pyplot as plt
import numpy as np

def total():
    number = int(input("Number: "))
    return number

def triangular_numbers():
    triangular_numbers = [(x * (x + 1) // 2) for x in range(1, total()+1)]
    return triangular_numbers

def Mobius_Matrix(lst):
    zeta_array = [[0 if n % m != 0 else 1 for n in lst] for m in lst]
    return Matrix(zeta_array) ** -1

M = Mobius_Matrix(triangular_numbers())
N = M[0, :].tolist()

plt.plot(N[0])
plt.show()