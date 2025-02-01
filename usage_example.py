
---

### 7. **usage_example.py**  
A script demonstrating how to use your package.

```python
from geometric_shapes.circle import Circle
from geometric_shapes.sphere import Sphere

def main():
    # Example for Circle
    try:
        circle = Circle(radius=5)
        print("Circle:")
        print(f"  Area: {circle.area():.2f}")
        print(f"  Perimeter: {circle.perimeter():.2f}")
    except Exception as e:
        print(f"Error creating Circle: {e}")

    # Example for Sphere
    try:
        sphere = Sphere(radius=5)
        print("\nSphere:")
        print(f"  Surface Area: {sphere.surface_area():.2f}")
        print(f"  Volume: {sphere.volume():.2f}")
    except Exception as e:
        print(f"Error creating Sphere: {e}")

if __name__ == "__main__":
    main()
