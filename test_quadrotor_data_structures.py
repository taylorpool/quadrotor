import pytest
import numpy as np
import quadrotor_data_structures as qds

def test_add_QuadrotorStateDerivative():
    d1 = qds.QuadrotorStateDerivative()
    d1.p_dot = np.array([1,1,1])
    d1.v_dot = np.array([1,1,1])
    d1.R_dot = np.eye(3)
    d1.omega_dot = np.array([1,1,1])
    d2 = qds.QuadrotorStateDerivative()
    d2.p_dot = np.array([2,2,2])
    d2.v_dot = np.array([2,2,2])
    d2.R_dot = -np.eye(3)
    d2.omega_dot = np.array([2,2,2])
    result = d1 + d2
    np.testing.assert_allclose(result.p_dot, d1.p_dot+d2.p_dot)
    np.testing.assert_allclose(result.v_dot, d1.v_dot+d2.v_dot)
    np.testing.assert_allclose(result.R_dot, d1.R_dot+d2.R_dot)
    np.testing.assert_allclose(result.omega_dot, d1.omega_dot+d2.omega_dot)