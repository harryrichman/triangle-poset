from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from Mobius_Matrix import Mobius_Matrix, triangular_numbers
from Absolute_Values import abs_value
from Sum_mobius_values import sum_function



M = Mobius_Matrix(triangular_numbers())
N = M[0, :].tolist()

S = sum_function(abs_value(N[0]))
plt.plot(S)
plt.show()
#slope approaching 0.5