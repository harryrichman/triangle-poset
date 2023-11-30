from sympy import *
import matplotlib.pyplot as plt
from mobius_matrix import mobius_matrix, triangular_numbers



def plot_matshow():
    M = mobius_matrix(triangular_numbers())
    M = M.transpose()
    plt.matshow(M)
    plt.tick_params(axis='both', which='major',
               labelsize=10, labelbottom=False,
               bottom=False, top=True, labeltop=True)
    plt.legend()
    plt.show()

plot_matshow()
