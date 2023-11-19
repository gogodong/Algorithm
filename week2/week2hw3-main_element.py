import numpy as np

arr = np.array([1,2,3,45,61,1,5,1])

stk = []
top = 0

for i in arr:
    stk.append(i)
    top = top + 1
    if top > 1:
        if stk[top-1] != stk[top-2]:
            stk.pop()
            stk.pop()
            top = top - 2

if len(stk)>0:
    print(stk[0])
else:
    print("No Main Element!")
