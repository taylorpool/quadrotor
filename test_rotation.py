import pytest
import numpy as np
import rotation

def test_skew():
    v = np.array([1.0, 0.0, 0.0])
    w = np.array([0.0, 1.0, 0.0])

    np.testing.assert_allclose(np.cross(v, w), rotation.skew(v)@w)