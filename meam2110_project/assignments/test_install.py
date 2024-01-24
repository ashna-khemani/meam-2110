print("\nTesting the ability to import pip installed packages ...")
import numpy
import matplotlib
import scipy
import meshcat
import sympy
import urchin 
print("\nSuccess!")

print("\nTesting proper setup of VSCode, and how the script is being run, by trying to import meam2110...")
from meam2110 import *
system = RigidBodySystem(visualize=False)
print("\nSuccess!")

print("\nYour VSCode setup should be ready to go.")
