from sympy import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from Mobius_Matrix import Mobius_Matrix
from Mobius_Matrix import triangular_numbers


def plot_sns():
    M = Mobius_Matrix(triangular_numbers())
    M = M.transpose()
    M = pd.DataFrame(M)
    #M.columns = triangular_numbers(n)
    sns.heatmap(M.corr())
    plt.tick_params(axis='both', which='major',
               labelsize=10, labelbottom=False,
               bottom=False, top=True, labeltop=True)
    plt.legend()
    plt.show()


plot_sns()
