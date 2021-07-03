Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> w1,w2,w3 = 0.3, 0.2, 0.5
>>> kanto_temp = 73
>>> kanto_rainfall = 67
>>> kanto_humidity = 43
>>> kanto_yield_apples = kanto_temp * w1 + kanto_rainfall * w2 + kanto_humidity * w3
>>> kanto_yield_apples
56.8
>>> print("The expected yield of apples in kanto region is {} tons per hectore", format)
The expected yield of apples in kanto region is {} tons per hectore <built-in function format>
>>> print("The expected yield of apples in kanto region is {} tons per hectore", format(kanto_yield_apples))
The expected yield of apples in kanto region is {} tons per hectore 56.8
>>> print(f"The expected yield of apples in kanto region is {kanto_yield_apples} tons per hectore")
The expected yield of apples in kanto region is 56.8 tons per hectore
>>> kanto = [73, 67, 43]
>>> johto = [91, 88, 64]
>>> sinnoh = [102, 43, 37]
>>> unova = [69, 96, 70]
>>> weights = [w1, w2, w3]
>>> def crop_yield(region, weights):
	result = 0
	for x, w in zip(region, weights):
		result += x*w
	return result

>>> crop_yield(johto, weights)
76.9
>>> crop_yield(unova, weight)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    crop_yield(unova, weight)
NameError: name 'weight' is not defined
>>> crop_yield(unova, weights)
74.9
>>> improt numpy as np
SyntaxError: invalid syntax
>>> improt pandas
SyntaxError: invalid syntax
>>> import numpy as np
>>> kanto = np.array([73,67,43])
>>> kanto
array([73, 67, 43])
>>> weight = np.array([w1, w2, w3])
>>> weight
array([0.3, 0.2, 0.5])
>>> type(kanto)
<class 'numpy.ndarray'>
>>> type(kanto)
<class 'numpy.ndarray'>
>>> np.dot(kanto, weight)
56.8
>>> kanto * weight
array([21.9, 13.4, 21.5])
>>> sum = kanto * weight
>>> sum
array([21.9, 13.4, 21.5])
>>> sum(sum)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sum(sum)
TypeError: 'numpy.ndarray' object is not callable
>>> sum.sum()
56.8
>>> arr2 = np.array(1,2,4)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    arr2 = np.array(1,2,4)
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
>>> arr1 = np.array([3,4,5])
>>> arr2 = np.array([1,6,7])
>>> arr3 = np.array([2,4,5,7])
>>> arr4 = arr1 * arr2
>>> arr4
array([ 3, 24, 35])
>>> arr5 = arr1 * arr3
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    arr5 = arr1 * arr3
ValueError: operands could not be broadcast together with shapes (3,) (4,) 
>>> 