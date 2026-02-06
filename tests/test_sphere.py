import pytest
import math
from geometry.sphere import volume_sphere


def test_volume_sphere_valid_input():
    """
    Test volume computation for a valid sphere radius.
    """
    radius = 3.0
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == expected


def test_volume_sphere_negative_radius():
    """
    Test behaviour when a negative radius is used.
    """
    with pytest.raises(ValueError):
        volume_sphere(-5.0)


def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius = 1.1
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
