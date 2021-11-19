import numpy as np
from dynamics import Dynamics
from quadrotor_data_structures import QuadrotorInput, QuadrotorStateDerivative, QuadrotorState
from rotation import skew
import dynamics_params as dp

class QuadrotorDynamics(Dynamics):
    def __init__(self):
        self.x = QuadrotorState()
        pass

    def dxdt(self, x: QuadrotorState, u: QuadrotorInput):
        z_w = np.array([0.0, 0.0, 1.0])
        z_b = x.R[:,2]
        x_dot = QuadrotorStateDerivative()
        x_dot.p_dot = x.v
        x_dot.v_dot = dp.g*z_w - u.c*z_b
        x_dot.R_dot = x.R@skew(x.omega)
        x_dot.omega_dot = np.linalg.solve(
            dp.J, 
            u.tau - np.cross(x.omega, dp.J@x.omega)
            )
        return x_dot