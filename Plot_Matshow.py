from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from Mobius_Matrix import Mobius_Matrix
from Mobius_Matrix import triangular_numbers


def plot_Mobius_values():
    M = Mobius_Matrix(triangular_numbers())
    M = M.transpose()
    plt.matshow(M)
    plt.tick_params(axis='both', which='major',
               labelsize=10, labelbottom=False,
               bottom=False, top=True, labeltop=True)
    plt.legend()
    plt.show()

plot_Mobius_values()
