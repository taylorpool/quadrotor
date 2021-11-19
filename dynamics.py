import numpy as np

class Dynamics:
    def __init__(self):
        self.x = [0.0, 0.0]
        self.m = 1.0
        pass

    def get_number_of_states(self):
        return len(self.x)

    def dxdt(self, x, u):
        return np.array([x[1], u[0]/self.m])

    def propogate_dynamics(self, u, dt):
        x_i = self.x

        k_1 = self.dxdt(x_i, u)
        k_2 = self.dxdt(x_i + .5*k_1*dt, u)
        k_3 = self.dxdt(x_i + .5*k_2*dt, u)
        k_4 = self.dxdt(x_i + k_3*dt, u)

        x_i += 1/6*(k_1+2*k_2+2*k_3+k_4)*dt
        self.x = x_i

        return self.x