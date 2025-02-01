from abc import ABC, abstractmethod

class BaseShape2D(ABC):
    """Abstract base class for 2D shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass

class BaseShape3D(ABC):
    """Abstract base class for 3D shapes."""

    @abstractmethod
    def surface_area(self) -> float:
        """Calculate the surface area of the shape."""
        pass

    @abstractmethod
    def volume(self) -> float:
        """Calculate the volume of the shape."""
        pass
