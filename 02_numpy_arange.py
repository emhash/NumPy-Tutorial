import numpy as np


# =-------ARANGE ------==
# syntax - arrange( start, stop ,)
ab = np.arange(10) #kinda like range()
# print(ab)

# syntax - arrange(start, stop, step)
# means starts from and stoped at. and the step between them is the last one

d1 = np.arange(10, dtype="complex")
# ^---> for this the syntax : arange(stop, dtype)

d2 = np.arange(1, 12, 2 , dtype="float")
# ^--> for this arange(start, stop, step, dtype)

# print(d2)
