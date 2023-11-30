import plotly.express as px
from sympy import *
from mobius_matrix import mobius_matrix, triangular_numbers


def plot_Mobius_values():
    M = mobius_matrix(triangular_numbers())
    M = M.transpose()
    fig = px.imshow(M, color_continuous_scale='RdBu', color_continuous_midpoint=0.0)
    fig.update_layout(
    xaxis={'side': 'top'})
    fig.show()


plot_Mobius_values()
