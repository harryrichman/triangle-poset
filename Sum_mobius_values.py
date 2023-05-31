from sympy import *
import matplotlib.pyplot as plt

number = int(input("Number: "))
triangular_numbers = ([(x * (x + 1) // 2) for x in range(1, number)])
def Mobius_Matrix(lst):
    zeta_array = [[0 if n % m != 0 else 1 for n in lst] for m in lst]
    return Matrix(zeta_array) ** -1
M = Mobius_Matrix(triangular_numbers)
N = M[0, :].tolist()

def sum_function(lst):
    sum_list = [sum(lst[:i+1]) for i in range(len(lst))]
    return sum_list

S = sum_function(N[0])
plt.plot(S)
plt.show