import numpy as np
import pandas as pd
# Q1.2P.1 --------------------------------------------------------------------------------------------------------------
another_array = np.zeros((2, 4, 6))
# Q1.2P.1(a)
# `import numpy as np` should be added before the original code.
# Q1.2P.1(b)
another_array[-1, :, :]
"""
Out[5]: 
array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])
"""
another_array[:, 0, :]
"""
Out[6]: 
array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])
"""
another_array[:, :, 2]
"""
Out[7]: 
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.]])
"""

# Q1.2P.2 --------------------------------------------------------------------------------------------------------------
"""
another_array = np.zeros((2, 4, 6))
new_array = another_array
new_array[1, 2, 2] = 1
print(another_array[1, 2, 2])
1.0
"""
# (1) This code does not make an independent copy of `another_array` named as `new_array`. `new_array` is actually a
# reference to the original array. (2) In R, when assigning the array to a new variable, it creates an independent new
# copy of the original array. (3) We may use `copy()` function.
new_array = another_array.copy()
new_array[1, 2, 2] = 1
print(another_array[1, 2, 2])
"""
0.0
"""

# Q1.2P.3 --------------------------------------------------------------------------------------------------------------
# The magic function `%paste` does not work in the Python script. `%paste` is not a standard Python command thus cannot
# be used in regular Python scripts.

# Q1.2P.4 --------------------------------------------------------------------------------------------------------------
# Change the working directory: %cd <path>
# Print the working directory: %pwd
# List the contents of working directory: %ls
# List current workspace variables: %who or %whos

# Q1.2P.5 --------------------------------------------------------------------------------------------------------------
"""
pip install pip-install-test
Collecting pip-install-test
  Downloading pip_install_test-0.5-py3-none-any.whl (1.7 kB)
Installing collected packages: pip-install-test
Successfully installed pip-install-test-0.5
Note: you may need to restart the kernel to use updated packages.
"""

# Q1.2P.6 --------------------------------------------------------------------------------------------------------------
# The original code returns nan because the `sample_scores` array contains a nan value.
sample_scores = np.array([1, 6, 7, 8, 9, np.nan])
print(np.nanvar(sample_scores))
"""
7.76
"""

# Q1.2P.7 --------------------------------------------------------------------------------------------------------------
nan_array = np.full((4, 3, 5), np.nan)
print(nan_array)
"""
[[[nan nan nan nan nan]
  [nan nan nan nan nan]
  [nan nan nan nan nan]]
 [[nan nan nan nan nan]
  [nan nan nan nan nan]
  [nan nan nan nan nan]]
 [[nan nan nan nan nan]
  [nan nan nan nan nan]
  [nan nan nan nan nan]]
 [[nan nan nan nan nan]
  [nan nan nan nan nan]
  [nan nan nan nan nan]]]
"""

# Q1.2P.8 --------------------------------------------------------------------------------------------------------------
# The additional step is `import pandas as pd`. I put it at the top of this script.
df = pd.read_csv('EuroNumbers_data.csv')
data_dict = df.to_dict()
keys = data_dict.keys()
print(keys)
"""
dict_keys(['Subject;RT;response;accuracy'])
"""

# Q1.2P.9 --------------------------------------------------------------------------------------------------------------
np.random.seed(1234)# Set the random seed
speed_sec = np.zeros(10)
sim_speed = np.random.uniform(size=5) # Speed simulation in seconds
speed_sec[0:5] = sim_speed * np.random.uniform(low=0.5, high=10, size=5)
speed_sec[5:10] = sim_speed

languages = ["R"] * 5 + ["Python"] * 5
code_types = [f"forloop{i}" for i in range(1, 6)] * 2

data_dict = {
    "language": languages,
    "code_type": code_types,
    "speed": speed_sec
}

df = pd.DataFrame(data_dict)
print(df)
"""
  language code_type     speed
0        R  forloop1  0.591724
1        R  forloop2  1.944967
2        R  forloop3  3.553380
3        R  forloop4  7.541267
4        R  forloop5  6.880447
5   Python  forloop1  0.191519
6   Python  forloop2  0.622109
7   Python  forloop3  0.437728
8   Python  forloop4  0.785359
9   Python  forloop5  0.779976
"""

# Q1.2P.10 -------------------------------------------------------------------------------------------------------------
# First take: 10.5/14; Second take: 12/14; Third Take: 14/14
# Revised the difference between matrix multiplication and element-wise multiplication and how to search for helps.