from setuptools import setup, find_packages

setup(
    name="python_geometrical_task",
    version="0.1.0",
    description="A project for geometric computations with 2D and 3D shapes",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add runtime dependencies if needed
    ],
    extras_require={
        "dev": [
            "pytest>=7.2",
            "pytest-cov>=4.0",
            "flake8>=6.0",
            "mypy>=1.0",
            "sphinx>=7.0",
            "pre-commit",
        ]
    },
    python_requires=">=3.8, <3.13",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
