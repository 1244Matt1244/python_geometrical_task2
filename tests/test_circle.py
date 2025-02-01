import pytest
from geometric_shapes.circle import Circle
from geometric_shapes.exceptions import InvalidDimensionError

def test_circle_area_and_perimeter():
    circle = Circle(5)
    assert pytest.approx(circle.area(), rel=1e-2) == 78.54  # π * 25 ≈ 78.54
    assert pytest.approx(circle.perimeter(), rel=1e-2) == 31.42  # 2 * π * 5 ≈ 31.42

def test_circle_invalid_radius():
    with pytest.raises(InvalidDimensionError):
        Circle(-1)
