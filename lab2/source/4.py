import numpy as np                       # importing the numpy packages

x = np.random.random(20)                 #generating random 20 values
print("Original array:\n ", x)

z = np.random.randint(20, size = 10)     #random (0-20)ranged 20 elements
print('\n\nranged input:',z)

b = np.bincount(z).argmax()              #finding the element freequently occuring
print('most repeated value is:',b)