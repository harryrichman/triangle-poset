from sympy import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from mobius_matrix import mobius_matrix, triangular_numbers


number = int(input("Number: "))


def plot_sns():
    M = mobius_matrix(triangular_numbers(number))
    M = M.transpose()
    M = pd.DataFrame(M)
    # M.columns = triangular_numbers(n)
    sns.heatmap(M.corr())
    plt.tick_params(
        axis="both",
        which="major",
        labelsize=10,
        labelbottom=False,
        bottom=False,
        top=True,
        labeltop=True,
    )
    plt.legend()
    plt.show()


plot_sns()
