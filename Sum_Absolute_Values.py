from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from mobius_matrix import mobius_matrix, triangular_numbers
from Absolute_Values import abs_value
from Sum_mobius_values import sum_function



number = int(input("Number: "))

M = mobius_matrix(triangular_numbers(number))
N = M[0, :].tolist()

S = sum_function(abs_value(N[0]))
plt.plot(S)
plt.show()
#slope approaching 0.5