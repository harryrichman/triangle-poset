from sympy import *
import matplotlib.pyplot as plt
from mobius_matrix import mobius_matrix, triangular_numbers


number = int(input("Number: "))

M = mobius_matrix(triangular_numbers(number))
N = M[0, :].tolist()

def partial_sums(lst):
    result = [sum(lst[:i+1]) for i in range(len(lst))]
    return result

n_divided = [N[i]/(i+1) for i in range(len(N))]

S = partial_sums(n_divided)

print(S[-1])
print(min(S))


plt.plot(S)
plt.show()