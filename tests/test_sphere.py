import pytest
from geometric_shapes.sphere import Sphere
from geometric_shapes.exceptions import InvalidDimensionError

def test_sphere_surface_area_and_volume():
    sphere = Sphere(5)
    assert pytest.approx(sphere.surface_area(), rel=1e-2) == 314.16  # 4 * π * 25 ≈ 314.16
    assert pytest.approx(sphere.volume(), rel=1e-2) == 523.60  # (4/3) * π * 125 ≈ 523.60

def test_sphere_invalid_radius():
    with pytest.raises(InvalidDimensionError):
        Sphere(0)
