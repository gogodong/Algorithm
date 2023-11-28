import numpy as np
import sys

INT_MAX = sys.maxsize
# global sum_inverse_pairs
sum_inverse_pairs = 0


def merge(arr1, arr2, length):
    len_arr1 = len(arr1)
    arr1.append(INT_MAX)
    arr2.append(INT_MAX)
    merge_tmp = []


    num_inverse_pairs = 0

    pt1 = 0
    pt2 = 0
    for i in range(length):
        if arr1[pt1] <= arr2[pt2]:
            merge_tmp.append(arr1[pt1])
            pt1 = pt1 + 1
        else:
            if arr[pt1] != INT_MAX:  # 排除最后的哨兵所造成的逆序对
                num_inverse_pairs += len_arr1 - pt1
            merge_tmp.append(arr2[pt2])
            pt2 = pt2 + 1

    return merge_tmp, num_inverse_pairs


def mergesort(arr, l, r):
    global sum_inverse_pairs  # 全局变量使用前一定要声明
    if l == r:
        return [arr[l]]
    mid = int((l + r) / 2)
    tmp1 = mergesort(arr, l, mid)
    tmp2 = mergesort(arr, mid + 1, r)

    arr_merge, num_inverse_pairs = merge(tmp1, tmp2, r - l + 1)

    sum_inverse_pairs += num_inverse_pairs

    return arr_merge

arr = [2,3,8,6,1]
mergesort(arr,0,len(arr)-1)
print(sum_inverse_pairs)