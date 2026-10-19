# Mass Balance Solver for a 2 component system
# 2 streams flow into a mixer, which feeds into a seperator

import numpy as np


A = np.array([[150,    0,    0],
               [  0,    1,    1],
               [-150, 0.8, 0.05]])

b = np.array([[ 50],
               [150],
                 [0]])

x = np.linalg.solve(A, b)
print(x)                        # where x is the matrix -> | x_3_ethanol |
                                #                          | x_4_flowrate|
                                #                          | x_5_flowrate|

# Validation

print(A @ x - b) # if correct will be equal to or near zero

print("The ethanol mass fraction of stream 3 is", x[0][0])
print("The mass flow rate of stream 4 is", x[1][0], "kg/h")
print("The mass flow rate of stream 5 is", x[2][0], "kg/h")