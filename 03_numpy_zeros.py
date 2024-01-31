import numpy as np


# =------- ZEROS ------==
# Syntax --> zeros(shape, dtype, order)
'''
This is about all are zero value

shape -- is the size or kind of range
dtype -- what data type it is 
order -- the order of the items like 'int','float' and so on

'''

d3 = np.zeros(3)
# print(d3)

d6 = np.zeros(4, order="F")
# print(d6)


# 2D zeros - here have to pass a tuple or list for (row , col )
# d4 = np.zeros((2,3),dtype="int")
d4 = np.zeros(shape=(2,3))
# or
d5 = np.zeros([2,3])

d7 = np.zeros(shape=[2,3],dtype="int")
# print(d7)


