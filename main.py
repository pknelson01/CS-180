import numpy as np
from typing import List
np.set_printoptions(edgeitems = 20, linewidth = 120, suppress = True)

# comment out
""" 
    SIG_FIG = 4

     x = [[ 0.9573075 ,  0.83877059,  1.51767182],
        #  [ 0.83782936, -0.88288659,  0.7371596 ],
        #  [-0.01786695,  0.83195016,  0.66394427],
        #  [-2.43495362, -0.5999003 , -1.40044824],
        #  [-0.67749399, -0.93229581,  0.4736418 ],
        #  [ 0.47934903,  0.90244159, -0.24246888],
        #  [ 1.00280715, -0.68745287, -1.08115248],
        #  [ 0.98143632,  0.77163722,  0.07051186],
        #  [ 1.10721349,  0.37520477,  0.54710493],
        #  [ 0.20813717, -0.56000733, -0.38301232]]
 
     averages = []

     for i in x:
        averages.append(np.mean(i))

    print(np.array(averages))
 
    print(np.zeros((3,5,3)))
    print(np.linspace(0, 10, 11))
    print(f"Identity Matrix (5):\n {np.eye(5)}")
    print(np.random.randn(4, 2))
    print(np.random.randint(1, 6, 3))
    arr = np.arange(100)
    print(arr.reshape(5,20))
 
    # arr = np.arange(7)
    print(arr, arr.argmax())
    print(arr, arr.argmin())

    ranarr = np.random.randint(1, 100, 10)
    print(ranarr, ranarr.argmax())
    print(ranarr, ranarr.argmin())
    print(ranarr, ranarr.max())
    print(ranarr, ranarr.min())
    print(ranarr.shape)
 
    print(arr, arr.shape)
    arr = arr.reshape(1,7)
    print(arr, arr.shape)

    print(arr.dtype)
 
    # arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    # print(arr, arr.shape)
    arr = arr.reshape(3,4)
    print(arr, arr.shape)
    print(np.array([10,11,12]))

    If it is a vector ([4,3,2,1]) then the shape will be incomplete (4,)
    if it is a matrix ([ [1,2,3], [4,5,6] ]) then the shape will be (2, 3)

    # x = np.array([ [1,2,3], [4,5,6] ])
    # print(x, x.shape)
"""

# a = np.arange(101)
# print(a[0:101:2])

b = np.eye(5, 5)
b = np.arange(25)
b = b.reshape(5,5)

print("first row: \n", b[0, :])
print("second row:\n", b[1, :])
print("third row:\n", b[2, :])
print("fourth row:\n", b[3, :])
print("last row:\n", b[4, :])
print("first column:\n", b[:, 0])
print("second column:\n", b[:, 1])
print("third column:\n", b[:, 2])
print("fourth column:\n", b[:, 3])
print("last column:\n", b[:, 4])
print("top-left 3x4: \n", b[0:3, 0:4])
print(b, "every-other row: \n", b[::2, :])
print("every-other column: \n", b[:, ::2])


