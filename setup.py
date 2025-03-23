from setuptools import setup

setup(
    name="pit",
    version="1.0.0",
    packages=["pit"],
    entry_points={"console_scripts": ["pit = src.cli:main"]},
)
