import numpy as np

a = np.array([1,2,3,4])
# print(a)

# =-------ARRAY ------==
a1 = np.array([1,2,4], "complex") #Here the complex is 'dtype' -> data type. means complex number type
# print(a1)

# ---- Slicing Array -----


arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# print(arr[1:6:2]) # This systax of slice -- [start         :        end           :  step]
                                            # start_from , end_step_one_step_ahead, step of gap
# print(arr[:3])

# MULTI SLICE
arr1 = np.array(
    [
        [0,1,2,3,4,5], 
        [6,7,8,9,10,11]
    ]
    )
# arr2 = np.array()

# print(arr1[:3 , 1:4]) ---> can not be like this . becouse of not name no of element

# print(arr1[:3 , 2:5]) #This 2nd half refers where to slice even if we declear in first half to slice from 0 to 2

# print(arr1[0:2, 0:2])

# --- Slice in one array from MULTI array ----
# syntax - array_name[index-of-first-array, slice-start : slice-end : step(optional)]

# print(arr1[0, 1:4])

# --------- METHODS ------
print("SHAPE of 1D array -> ",np.shape(arr))
print("SHAPE -> ",np.shape(arr1))
print("SIZE of 1D array-> ",np.size(arr))
print("SIZE -> ",np.size(arr1))
print("Dimantion -> ",np.ndim(arr1))
print("Type -> ",arr1.dtype)

# more ex - len(), astype()
print("Elements in 2D array --> ", np.size(arr1)) 
# We can remember as each array in multi 2D array has same elements 
# so first array's elements are same as other all index's array. 
# ex - [1 2 3] = 3 elem. [4 5 6] = also 3 elem.