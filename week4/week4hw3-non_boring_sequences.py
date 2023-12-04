def solve_problem(left, right):
    if left >= right:
        return True  # 如果递归到只剩一个元素，那么此时肯定是不无聊的
    else:
        for i in range(right - left):
            if prepos[left + i] < left and nextpos[left + i] > right:  # 如果在左侧找到了，那么就直接一分为二，进入下一次遍历
                return solve_problem(left, left + i) and solve_problem(left + i + 1, right)
            if prepos[right - i - 1] < left and nextpos[right - i - 1] > right:  # 如果在右侧找到了，同样的操作
                return solve_problem(left, left + i) and solve_problem(left + i + 1, right)
        return False  # 如果遍历完都没有找到，那么也就是无聊序列


arr = [1, 2, 3, 2, 1]

arr_dic = {}  # 该字典的作用是暂存遍历到的某一数组元素的位置。在下一次再次遍历到该元素时，才将其值赋给prepos或者nextpos。这保证了对于单独一个元素，prepos或者nextpos是-1或者MAX
prepos, nextpos = [], []

len_arr = len(arr)
INT_MAX = len_arr + 1

for i in range(len_arr):
    if arr_dic.get(arr[i]) is None:
        prepos.append(-1)  # 如果是第一次找到该元素，那么定义该元素上一个为-1，并且将当前的下标记录在arr_dict中
    else:
        prepos.append(arr_dic.get(arr[i]))  # 当前元素arr[i]如果不是第一次，那就把之前记录的“当前位置”作为prepos记录进去
    arr_dic[arr[i]] = i  # 无论如何，都要更新当前下标

arr_dic.clear()

for i in range(len_arr):
    if arr_dic.get(arr[len_arr - i - 1]) is None:
        nextpos.append(INT_MAX)
    else:
        nextpos.append(arr_dic.get(arr[len_arr - i - 1]))
    arr_dic[arr[len_arr - i - 1]] = len_arr - i - 1
nextpos.reverse()

if solve_problem(0, len_arr):
    print("No boring")
else:
    print("Boring!")
