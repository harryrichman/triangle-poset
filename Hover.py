from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mplcursors

def triangular_numbers(n):
    # returns a list of triangular numbers
    return [(x * (x + 1) // 2) for x in range(1, n+1)]

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
    M = pd.DataFrame(M)
    M.columns = triangular_numbers(n)
    corr = M.corr()
    
    fig, ax = plt.subplots()
    cax = ax.imshow(corr, cmap="magma")
    plt.colorbar(cax, label="Correlation")
    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(corr.columns)
    plt.show()
    
    fig, ax = plt.subplots()
    cax = ax.imshow(corr, cmap='coolwarm')
    plt.colorbar(cax, label="Correlation")
    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(corr.columns)
    mplcursors.cursor(ax, hover=True)
    plt.show(block=True)

plot_Mobius_values(int(input("Number: ")))