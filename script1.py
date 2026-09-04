import numpy as np
import math

#a = np.array([1, 2, 3])
#print(a)

# ---------- Dimensions of an array ----------
#print(a.ndim)

# ---------- Multi-dimensional array ----------
#b = np.array([[1,2,3],[4,5,6]])
#print(b)
#print(b.ndim) # Dimensions of b
#print(b.shape) # Returns the length of each dimension
#print(b.dtype) # Returns the type of items in the array

# ---------- We can also put floats in a numpy array ----------
#c = np.array([2.2, 5, 1.1]) # Numpy will convert 5 into an integer to keep the data types homogeneous
#print(c.dtype)

# ---------- If we don´t know what to put inside of our array, we can create arrays with initial placeholders ----------
#d = np.zeros((2,3)) # An array with 0´s
#print(d)

#e = np.ones((2,3)) # An array with 1´s
#print(e)

#f = np.random.rand(2,3) # An array with random numbers
#print(f)

# ---------- arange() ----------
# Creates a sequence of numbers in an array
# arange(starting bound inclusive, ending bound exclusive, step)
#g = np.arange(10, 50, 2)
#print(g)

# ---------- linspace() ----------
# Same as arange except because of the third argument
# The third argument is the total of items we want to generate between the range
# In this case, the range is inclusive in the start and the end
#h = np.linspace(0 , 2, 15)
#print(h)

# ------------------------------------------------------------
#a = np.array([10, 20, 30, 40, 50])
#b = np.array([1, 2, 3, 4, 5])

# ---------- sustraction ----------
#c = a - b
#print(c)

# ---------- multiplication ----------
#d = a * b
#print(d)

# ---------- addition ----------
#e = a + b
#print(e)

# ---------- example ----------
#farenheit = np.array([0, -10, -5, -15, 0])
#celcius = (farenheit - 31) * (5/9)
#print(celcius)

# ---------- example with a boolean array ----------
#boolean_array = celcius > -20
#print(boolean_array)

# ---------- module ----------
#module_array = celcius % 2
#print(module_array)

# ---------- elementwise product ----------
#A = np.array([[1,1], [0,1]])
#B = np.array([[2,0], [3,4]])
#print(A * B)

# ---------- matrix product ----------
#print(A @ B)

# ---------- .shape ----------
# .shape returns the matrix dimension
#print(A.shape)

# ----------------------------------------
#array1 = np.array([[1, 2, 3], [4, 5, 6]])
#array2 = np.array([[7.1, 8.2, 9.1], [10.4, 11.2, 12.3]])
#array3 = array1 + array2

# ---------- sum() ----------
#print(array3.sum()) #return the sum of the elements

# ---------- max() ----------
#print(array3.max())

# ---------- min() ----------
#print(array3.min())

# ---------- mean() ----------
#print(array3.mean()) #return the average of the elements

# All of the above operations are allowed for two dimensional arrays

# ---------- Indexing ----------
#a = np.array([1, 3, 5, 7])
#print(a[2])

#a = np.array([[1,2], [3,4], [5,6]])
#print(a[1,1])

#b = np.array([a[0,0], a[1,1], a[2,1]])
#print(b)

#print(a[[0 ,1 ,2], [0, 1, 1]])
#print(a)

# ---------- Boolean Indexing ----------
#print(a > 5)

#print(a[a > 5])

# ---------- Slicing ----------
#a = np.array([0, 1, 2, 3, 4, 5])

#print(a[:3])
#print(a[2:3])

#a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#print(a[:2])
#print(a[:2, 1:3])
#sub_array = a[:2, 1:3]
#print(f"sub array index [0,0] value before change: {sub_array[0,0]}")
#sub_array[0,0] = 50
#print(f"sub array index [0,0] value after change: {sub_array[0,0]}")

#import pandas as pd

#pd.


















