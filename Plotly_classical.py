import plotly.express as px
from sympy import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def Zeta_Matrix(n):
    # returns zeta matrix for partial order on first n numbers
    lst = range(1, 1 + n)
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
    M = M.transpose()
    fig = px.imshow(M, color_continuous_scale='RdBu', color_continuous_midpoint=0.0)
    fig.show()


plot_Mobius_values(int(input("Number: ")))
