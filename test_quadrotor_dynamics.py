from dynamics import Dynamics
import pytest
from itertools import product
import numpy as np
from quadrotor_data_structures import QuadrotorState, QuadrotorStateDerivative, QuadrotorInput
from quadrotor_dynamics import QuadrotorDynamics
import dynamics_params as dp

def test_dxdt():
    dynamics = QuadrotorDynamics()
    x = QuadrotorState()
    true_dxdt = QuadrotorStateDerivative()
    u = QuadrotorInput()
    x_dot = dynamics.dxdt(x, u)
    np.testing.assert_allclose(x_dot.p_dot, np.zeros(3))
    np.testing.assert_allclose(x_dot.v_dot, np.array([0.0, 0.0, dp.g]))
    np.testing.assert_allclose(x_dot.R_dot, np.zeros((3,3)))
    np.testing.assert_allclose(x_dot.omega_dot, np.zeros(3))

def test_propogate_dynamics():
    dynamics = QuadrotorDynamics()
    u = QuadrotorInput()

    result = dynamics.propogate_dynamics(u, 1.0)