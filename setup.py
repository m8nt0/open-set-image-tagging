from setuptools import setup, find_packages

setup(
    name="recognize-anything",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "flask",
        "opencv-python",
        "numpy",
        "pandas",
    ],
)
