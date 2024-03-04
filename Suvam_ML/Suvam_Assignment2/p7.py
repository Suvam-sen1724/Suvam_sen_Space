"""
Question 7:
Write a Python program to calculate the determinant and inverse of a given matrix. (Use
SciPy)
A = 
[[3, 2, -1],
[2, -4, 7],
[1, 1, 1]]

"""
import scipy as sp

A = [[3, 2, -1],
     [2, -4, 7],
     [1, 1, 1]]

determinant = sp.linalg.det(A)

print("Determinant of the matrix: ",determinant)

inverse = sp.linalg.inv(A)

print("Inverse of the Matrix:\n",inverse)

"""
Answer:
Determinant of the matrix:  -28.999999999999996
Inverse of the Matrix:
 [[ 0.37931034  0.10344828 -0.34482759]        
 [-0.17241379 -0.13793103  0.79310345]
 [-0.20689655  0.03448276  0.55172414]]
"""