
import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Generating an array with zeros
zero_arr = np.zeros((3, 3))
print("Zero Array:", zero_arr)

# Generating an array with ones
ones_arr = np.ones((3, 3))
print("Ones Array:", ones_arr)

# Generating an identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:", identity_matrix)

# Generating an array with random values
random_arr = np.random.rand(3, 3)
print("Random Array:", random_arr)

# Array Slicing
sliced_arr = arr[1:4]
print("Sliced Array:", sliced_arr)

# Reshaping an array
reshaped_arr = arr.reshape(1, 5)
print("Reshaped Array:", reshaped_arr)

# Array Operations (Element-wise)
sum_arr = arr + arr
print("Sum of Arrays:", sum_arr)

# Dot Product
dot_product = np.dot(arr, arr)
print("Dot Product:", dot_product)

# Finding the mean of an array
mean_val = np.mean(arr)
print("Mean:", mean_val)

# Finding the standard deviation of an array
std_dev = np.std(arr)
print("Standard Deviation:", std_dev)
