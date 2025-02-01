import argparse
from .circle import Circle
from .sphere import Sphere

def main():
    parser = argparse.ArgumentParser(description="Geometric Shapes CLI")
    parser.add_argument("--shape", choices=["circle", "sphere"], required=True, help="Shape type")
    parser.add_argument("--radius", type=float, required=True, help="Radius of the shape")
    args = parser.parse_args()

    if args.shape == "circle":
        shape = Circle(args.radius)
        print(f"Circle with radius {args.radius}:")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
    elif args.shape == "sphere":
        shape = Sphere(args.radius)
        print(f"Sphere with radius {args.radius}:")
        print(f"  Surface Area: {shape.surface_area():.2f}")
        print(f"  Volume: {shape.volume():.2f}")

if __name__ == "__main__":
    main()
