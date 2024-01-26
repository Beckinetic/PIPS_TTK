import numpy as np
from datetime import datetime
import time
import warnings

# Q2.2P.1 --------------------------------------------------------------------------------------------------------------
if 0 <= datetime.now().hour < 5:
    print("Go to sleep!")
elif 7 <= datetime.now().hour < 10:
    print("Eet je hagelslag!")
else:
    print("Gut gemacht!")

# Q2.2P.2 --------------------------------------------------------------------------------------------------------------
numeric_vec = np.random.uniform(low=0, high=100, size=4)
weight_sum = 0
for i in range(numeric_vec.size):
    weight_sum = weight_sum + numeric_vec[i] * (i % 2 * 2)
weight_avg = weight_sum / (numeric_vec.size * 1.5)

# Q2.2P.3 --------------------------------------------------------------------------------------------------------------
# Q2.2P.3(a)
# This code cannot run in Python. It returns error messages:

# Traceback (most recent call last):
#   File "/Users/luoyifan/opt/anaconda3/envs/py310/lib/python3.10/site-packages/IPython/core/interactiveshell.py", line 3369, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-20-9b9ae2d61b7a>", line 12, in <cell line: 12>
#     these_items = color_it(sky, ground)
#   File "<ipython-input-20-9b9ae2d61b7a>", line 4, in color_it
#     grass_me = grass
# UnboundLocalError: local variable 'grass' referenced before assignment

# This is different from the similar R code. In this Python code, inside the function `color_it` the input argument will
# not be assigned with the value of global variable grass. The scope of the function is quarantined from the outside
# environment unless it's input.
# Q2.2P.3(b)
grass = "green"

def color_it(color_me, grass_me):
    # grass_me = grass
    color_me = "blue"
    grass = "blue"
    colorful_items = np.array([(color_me, grass_me)])
    return colorful_items

sky = "grey"
ground = "brown"
these_items = color_it(sky, ground)
print(these_items)

# Q2.2P.4 --------------------------------------------------------------------------------------------------------------
# Q2.2P.4(a)
def special(vec):
    uniq_vals = []
    for i in range(vec.size):
        if not (vec[i] in uniq_vals):
            uniq_vals.append(vec[i])
    return uniq_vals
# Q2.2P.4(b)
def special(vec):
    if not isinstance(vec, np.ndarray):
        raise Exception("vec must be an array")

    uniq_vals = []
    for i in range(vec.size):
        if not (vec[i] in uniq_vals):
            uniq_vals.append(vec[i])
    return uniq_vals
# Q2.2P.4(c)
def special(vec):
    if not isinstance(vec, np.ndarray):
        raise Exception("vec must be an array")

    uniq_vals = []
    warning_flag = True
    for i in range(vec.size):
        if not (vec[i] in uniq_vals):
            uniq_vals.append(vec[i])
        elif (vec[i] in uniq_vals):
            warning_flag = False

    if warning_flag:
        warnings.warn("All values are special!")
    return uniq_vals

# Q2.2P.5 --------------------------------------------------------------------------------------------------------------
# Q2.2P.5(a)
# (1) The try block lets you test a block of code for errors.
# (2) The except block lets you handle the error."
# source: https://www.w3schools.com/python/python_try_except.asp
# Q2.2P.5(b)
def special(vec):
    try:
        if not isinstance(vec, np.ndarray):
            raise Exception("vec must be an array")

        uniq_vals = []
        for i in range(vec.size):
            if not (vec[i] in uniq_vals):
                uniq_vals.append(vec[i])
        return uniq_vals
    except Exception as e:
        raise Exception("An error occured while running special")

# Q2.2P.6 --------------------------------------------------------------------------------------------------------------
class MyClass:
    """A simple example class"""
    classnum = 12345

    def famous(self):
        return 'hello world'
new_stuff = MyClass()
new_stuff.classnum
new_stuff.famous()
# Out[36]: 'hello world'
# (1) A Python class is a blueprint for creating objects, combining data and functions.
# (2) It allows for the creation of multiple instances, each with its own attributes and methods.
# (3) Classes enable inheritance, permitting new classes to derive properties from existing ones. This mechanism is
# dynamic, supporting modifications even after class creation.

# Complex number class
class ComplexNum:
    """Creates a complex number"""
    numtype = 'complex'
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def vec_length(self):
        return np.sqrt(self.r**2 + self.i**2)

    def phase_angle(self):
        return np.arctan(self.i / self.r) / np.pi * 180

my_num = ComplexNum(3.0, 4.0)
print(my_num)
print((my_num.r, my_num.i))
print(my_num.numtype)
print(my_num.vec_length())
print(my_num.phase_angle())

# Q2.2P.7 --------------------------------------------------------------------------------------------------------------
# I was a bit confused about how the question was framed ("that calculates, by iteration, the number to the nth power
# using Newton’s method") because the Newton's method is usually applied in calculating the value of roots. But since
# power and root are actually interchangeable I write the function anyway, though the formulas seem different from what
# is its most common version.
def nthpower(number, n, start=1):
    max_iterations = 10000
    iteration = 0
    tolerance = 1e-6

    x = start
    while iteration < max_iterations:
        iteration = iteration + 1
        f_x = x ** (1/n) - number
        f_prime_x = (1/n) * x ** ((1/n) - 1)

        x_new = x - f_x / f_prime_x
        if abs(x_new - x) < tolerance:
            break
        x = x_new

    return x

# Q2.2P.8 --------------------------------------------------------------------------------------------------------------
def prime(n):
    """
    Generate the first 'n' prime numbers starting from 2.
    Parameters:
    n (int): A positive integer specifying the number of prime numbers to generate.
    Returns:
    numpy.ndarray: An array of the first 'n' prime numbers.
    Example:
    prime(10)
    array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    """
    try:
        if n < 1:
            raise ValueError('n must be greater than 1')

        prime_list = np.array([2])
        x = 3
        while (len(prime_list) < n):
            for i in prime_list:
                if x % i == 0:
                    # x is not a prime number
                    break
                if i == prime_list[-1]:
                    # x is a prime number, append it to the array
                    prime_list = np.append(prime_list, x)
            x += 1
        return prime_list
    except Exception as e:
        raise Exception(e)

# Q2.2P.9 --------------------------------------------------------------------------------------------------------------
# ?prime
# Signature: prime(n)
# Docstring:
# Generate the first 'n' prime numbers starting from 2.
# Parameters:
# n (int): A positive integer specifying the number of prime numbers to generate.
# Returns:
# numpy.ndarray: An array of the first 'n' prime numbers.
# Example:
# prime(10)
# array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
# File:      ~/Library/CloudStorage/OneDrive-Personal/ResMasPsych/1 - Course Files/Programming in Psychological Science/asgP/sequences.py
# Type:      function
