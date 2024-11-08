import plotly.express as px
from sympy import *
import numpy as np
from mobius_matrix import mobius_matrix, triangular_numbers


def plotly_classical():
    M = mobius_matrix(triangular_numbers())
    # M = M.transpose()
    fig = px.imshow(
        M, color_continuous_scale="RdBu", color_continuous_midpoint=0.0, zmin=-2, zmax=2
    )
    fig.update_layout(xaxis={"side": "top"})
    fig.show()


plotly_classical()
