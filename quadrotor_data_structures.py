import numpy as np

class QuadrotorState:
    def __init__(self):
        self.p = np.zeros(3)
        self.v = np.zeros(3)
        self.R = np.eye(3, dtype=np.float64)
        self.omega = np.zeros(3)

class QuadrotorStateDerivative:
    def __init__(self):
        self.p_dot = np.zeros(3)
        self.v_dot = np.zeros(3)
        self.R_dot = np.zeros((3,3), dtype=np.float64)
        self.omega_dot = np.zeros(3)

    def __add__(self, other):
        result = QuadrotorStateDerivative()
        result.p_dot = self.p_dot + other.p_dot
        result.v_dot = self.v_dot + other.v_dot
        result.R_dot = self.R_dot + other.R_dot
        result.omega_dot = self.omega_dot + other.omega_dot
        return result

    def __mul__(self, other):
        if type(other) == float:
            result = QuadrotorStateDerivative()
            result.p_dot = other*self.p_dot
            result.v_dot = other*self.v_dot
            result.R_dot = other*self.R_dot
            result.omega_dot = other*self.omega_dot
            return result
        else:
            raise Exception('Invalid operand')
        end


class QuadrotorInput:
    def __init__(self, c=0.0, tau=np.zeros(3)):
        self.c = c
        self.tau = tau