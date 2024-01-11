from sympy import *
import matplotlib.pyplot as plt
import numpy as np

def triangular_numbers(n):
    triangular_numbers = [(x * (x + 1) // 2) for x in range(1, n+1)]
    return triangular_numbers

def mobius_matrix(lst):
    zeta_array = [[0 if n % m != 0 else 1 for n in lst] for m in lst]
    Z = np.array(zeta_array)
    Z.transpose()
    return np.linalg.inv(Z)

if __name__ == "__main__":
    
    number = int(input("Number: "))
    M = mobius_matrix(triangular_numbers(number))
    N = M[0, :].tolist()

    plt.plot(N[0])
    plt.show()