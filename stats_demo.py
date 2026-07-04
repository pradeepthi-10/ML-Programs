import statistics
data=[10,20,30,40,90]
print("mean:",statistics.mean(data))
print("median:",statistics.median(data))
print("mode:",statistics.mode(data))

import math
num = 25
print("Square Root:", math.sqrt(num))
print("Power (5^2):", math.pow(5, 2))
print("Factorial of 5:", math.factorial(5))
print("Value of Pi:", math.pi)
print("Value of e:", math.e)
print("Ceil of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))
 
from scipy import stats
data = [10, 20, 30, 40, 50]
print("Mean:", stats.tmean(data))
print("Variance:", stats.tvar(data))
print("Standard Deviation:", stats.tstd(data))

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))


import statistics
import math
import numpy as np
from scipy import stats

# Sample Data
data = [10, 20, 30, 40, 50]

# Statistics Library
print("=== Statistics Library ===")
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))

# Math Library
print("\n=== Math Library ===")
print("Square Root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Value of Pi:", math.pi)

# NumPy Library
arr = np.array(data)
print("\n=== NumPy Library ===")
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# SciPy Library
print("\n=== SciPy Library ===")
print("Mean:", stats.tmean(data))
print("Variance:", stats.tvar(data))
print("Standard Deviation:", stats.tstd(data))