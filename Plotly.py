import plotly.express as px
from sympy import *
from Mobius_Matrix import Mobius_Matrix
from Mobius_Matrix import triangular_numbers

def plot_Mobius_values():
    M = M = Mobius_Matrix(triangular_numbers())
    M = M.transpose()
    fig = px.imshow(M, color_continuous_scale='RdBu', color_continuous_midpoint=0.0)
    fig.update_layout(
    xaxis={'side': 'top'})
    fig.show()


plot_Mobius_values()
