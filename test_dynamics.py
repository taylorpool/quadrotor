import pytest
from scipy.integrate import RK45
from itertools import product
import numpy as np
from dynamics import Dynamics

@pytest.mark.skip
@pytest.mark.parametrize("x, u", 
    product(np.random.random((3, 2)), np.random.random((3,1))) )
def test_dxdt(x, u):
    dynamics = Dynamics()
    true_dxdt = np.array([x[1], u[0]/dynamics.m])
    dxdt =  dynamics.dxdt(x, u)
    np.testing.assert_allclose(dxdt, true_dxdt)

@pytest.mark.skip
@pytest.mark.parametrize("u, dt", 
    product(
        np.random.random((3,1)),
        np.linspace(0, 10, 5)
        ) 
)
def test_propogate_dynamics(u, dt):
    dynamics = Dynamics()
    true_x = np.array([0.5*u[0]/dynamics.m*dt**2, u[0]/dynamics.m*dt])
    x = dynamics.propogate_dynamics(u, dt)
    np.testing.assert_allclose(x, true_x)

