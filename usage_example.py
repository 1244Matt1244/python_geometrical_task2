from geometric_shapes.circle import Circle
from geometric_shapes.sphere import Sphere

def main():
    # Example for Circle
    try:
        circle = Circle(radius=5)
        print(f"Circle with radius {circle.radius}:")
        print(f"  Area: {circle.area():.2f}")
        print(f"  Perimeter: {circle.perimeter():.2f}")
    except Exception as e:
        print(f"Error creating Circle: {e}")

    # Example for Sphere
    try:
        sphere = Sphere(radius=5)
        print(f"\nSphere with radius {sphere.radius}:")
        print(f"  Surface Area: {sphere.surface_area():.2f}")
        print(f"  Volume: {sphere.volume():.2f}")
    except Exception as e:
        print(f"Error creating Sphere: {e}")

if __name__ == "__main__":
    main()
