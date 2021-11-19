import numpy as np

m = 1.0
J = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
])
g = 9.81
k_F = 1.0
k_M = 1.0
r_1 = np.array([0.25, 0.25, 0.0])
r_2 = np.array([-0.25, 0.25, 0.0])
r_3 = np.array([-0.25, -0.25, 0.0])
r_4 = np.array([0.25, -0.25, 0.0])

motor_u_omega = np.array([
    [k_F, k_F, k_F, k_F],
])