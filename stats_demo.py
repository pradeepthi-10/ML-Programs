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