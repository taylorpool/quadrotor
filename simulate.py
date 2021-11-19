import numpy as np
from dynamics import Dynamics
from controller import Controller
import time_params as default_time_params

class Simulator:
    def __init__(self, dynamics, controller, time_params = default_time_params):
        self.dynamics = dynamics
        self.controller = controller
        self.dt = time_params.dt
        self.times = np.arange(time_params.t0, time_params.tf, time_params.dt)
        self.x_s = np.zeros((len(self.times), self.dynamics.get_number_of_states()), dtype=np.float64)
        self.u_s = np.zeros((len(self.times), 1))

    def step(self, x, u, dt):
        new_x = self.dynamics.propogate_dynamics(u, dt)
        new_u = self.controller.get_controls(x)
        return new_x, new_u
    
    def simulate(self):
        i = 0
        for x, u in zip(self.x_s, self.u_s):
            new_x, new_u = self.step(x, u, self.dt)
            self.x_s[i+1] = new_x
            self.u_s[i+1] = new_u
            i += 1

        return times, x_s, u_s


if __name__ == '__main__':
    dynamics = Dynamics()
    controller = Controller()
    simulator = Simulator(dynamics, controller)
    times, x_s, u_s = simulator.simulate()