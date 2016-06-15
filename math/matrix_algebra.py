# Matrix Algebra

import numpy as np
#input matrices

A = np.array([1,2,3,2,7,4]).reshape(2,3)
B = np.array([1,-1,0,1]).reshape(2,2)
C = np.array([5,-1,9,1,6,0]).reshape(3,2)
D = np.array([3,-2,-1,1,2,3]).reshape(2,3)
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5]).reshape(4,1)


# 1. Matrix Dimensions
# 1.1: 2 x 3
# 1.2: 2 x 2
# 1.3: 3 x 2
# 1.4: 2 x 3
# 1.5: 1 x 4
# 1.6: 4 x 1

# 2. Vector Operations
# 2.1 [9, 7, -4, 9]
u + v
array([ 9,  7, -4,  9])

# 2.2 [3, -3, -2, 1]
u - v
array([ 3, -3, -2,  1])

#2.3 [36, 12, -18, 30]
alpha = 6
alpha*u
array([ 36,  12, -18,  30])

# 2.4 [51]
np.dot(u, v)
51

# 2.5  8.6
np.linalg.norm(u)
8.6023252670426267

#3 Matrix Operations

#3.1  undefined
A + C
#ValueError: operands could not be broadcast together with shapes (2,3) (3,2) 

#3.2   
# [[-4, -7, -3],
#  [3, 6, 4]]
A - C.transpose()
array([[-4, -7, -3],
       [ 3,  6,  4]])
       
#3.3 [[14, 3, 3,],
#     [2, 7, 9]]
C.transpose() + 3*D
array([[14,  3,  3],
       [ 2,  7,  9]])
       
# 3.4 [[-1, -5, -1],
#      [2, 7, 4]]
np.dot(B,A)
array([[-1, -5, -1],
       [ 2,  7,  4]])
       
# 3.5   not defined
np.dot(B, A.transpose())
#ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# 3.6   not defined
np.dot(B, C)
#ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# 3.7  [[5, -6],
#      [9, -8],
#      [6, -6]]
np.dot(C, B)
array([[ 5, -6],
       [ 9, -8],
       [ 6, -6]])
       
# 3.8 [[1,1],
#     [0,1]]
B**4
array([[1, 1],
       [0, 1]])
       
# 3.9   [[14, 28],
#        [28, 69]]
np.dot(A, A.transpose())
array([[14, 28],
       [28, 69]])
       
# 3.10   [[10, -4, 0],
#        [-4, 8, 8],
#        [0, 8, 10]]
np.dot(D.transpose(), D)
array([[10, -4,  0],
       [-4,  8,  8],
       [ 0,  8, 10]])
