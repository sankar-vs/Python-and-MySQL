'''
@Author: Sankar
@Date: 2021-04-13 21:50:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-13 21:55:09
@Title : Numpy_Python-4
'''
'''
Write a Python program to reverse an array (first element becomes last).
Original array:
[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
Reverse array:
[37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]
'''
import numpy as np
x = np.arange(12,38)
print(x)
print(x[::-1])