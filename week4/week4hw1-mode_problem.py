import numpy as np
import sys

INT_MAX = sys.maxsize
problem = np.random.randint(1, 5, size=10)
print(problem)


# 利用哨兵机制，使代码容易读懂一些
def merge(arr1, arr2, length):
    arr1.append(INT_MAX)
    arr2.append(INT_MAX)
    merge_tmp = []

    pt1 = 0
    pt2 = 0
    for i in range(length):
        if arr1[pt1] <= arr2[pt2]:
            merge_tmp.append(arr1[pt1])
            pt1 = pt1 + 1
        else:
            merge_tmp.append(arr2[pt2])
            pt2 = pt2 + 1

    return merge_tmp


def mergesort(arr, l, r):
    if l == r:
        return [arr[l]]
    mid = int((l + r) / 2)
    tmp1 = mergesort(arr, l, mid)
    tmp2 = mergesort(arr, mid + 1, r)

    arr_merge = merge(tmp1, tmp2, r - l + 1)

    return arr_merge


arr_sorted = mergesort(problem, 0, len(problem) - 1)

# 在末尾添加一个哨兵
arr_sorted.append(INT_MAX)

ptl = 0
ptr = 1
cnt_max = 1
pt = 0  # 存储众数的指针

# 使用类似擂台，遍历一遍数组得到众数，其实使用字典会更加容易读
for i in range(len(arr_sorted) - 1):
    if arr_sorted[ptl] == arr_sorted[ptr]:
        ptr = ptr + 1
    else:

        # 如果这个数的重数更多，那么更新其重数，并且保存该数
        if (ptr - ptl) > cnt_max:
            cnt_max = ptr - ptl
            pt = ptl
        ptl = ptr
        ptr = ptr + 1

print("众数是：%d,其重数是：%d.\n" % (arr_sorted[pt], cnt_max))
