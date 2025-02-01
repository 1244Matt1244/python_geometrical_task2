def print_shape_info(shape):
    """Prints formatted information about a shape."""
    info = (
        f"Area: {shape.area():.2f}" if hasattr(shape, "area") else f"Surface Area: {shape.surface_area():.2f}"
    )
    print(info)
