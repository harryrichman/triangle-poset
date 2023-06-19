from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from Mobius_Matrix import Mobius_Matrix
from Absolute_Values import abs_value
from Sum_mobius_values import sum_function

number = int(input("Number: "))
triangular_numbers = ([(x * (x + 1) // 2) for x in range(1, number+1)])

M = Mobius_Matrix(triangular_numbers)
N = M[0, :].tolist()

S = sum_function(abs_value(N[0]))
slope = (S[-1] - S[0])/(number - 0)
print(slope)
plt.plot(S)
plt.show()
#slope approaching 0.5