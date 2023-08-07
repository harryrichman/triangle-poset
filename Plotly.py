import plotly.express as px
from sympy import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def triangular_numbers(n):
    # returns a list of triangular numbers
    return [(x * (x + 1) // 2) for x in range(1,n+1)]

def Zeta_Matrix(n):
    # returns zeta matrix for partial order on first n triangular numbers
    lst = triangular_numbers(n)
    zeta_array = [[0 if a % b != 0 else 1 for a in lst] for b in lst]
    Z = np.array(zeta_array)
    Z.transpose()
    return Z

def Mobius_Matrix(a):
    Z = Zeta_Matrix(a)
    M = np.linalg.inv(Z)
    return M

def plot_Mobius_values(n):
    M = Mobius_Matrix(n)
    fig = px.imshow(M, color_continuous_scale='RdBu', color_continuous_midpoint=0.0)
    fig.show()


plot_Mobius_values(int(input("Number: ")))
