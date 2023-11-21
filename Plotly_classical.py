import plotly.express as px
from sympy import *
import numpy as np
from Mobius_Matrix import Mobius_Matrix
from Mobius_Matrix import triangular_numbers


def plotly_classical():
    M = Mobius_Matrix(triangular_numbers())
    #M = M.transpose()
    fig = px.imshow(M, color_continuous_scale='RdBu', color_continuous_midpoint=0.0, zmin=-2, zmax=2)
    fig.update_layout(
    xaxis={'side': 'top'}  
)
    fig.show()


plotly_classical()
