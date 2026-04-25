from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-JENKINS",
    version="0.1",
    author="Vel",
    packages=find_packages(),
    install_requires = requirements,
)