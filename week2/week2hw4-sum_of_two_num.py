import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

front = 0
rear = len(arr) - 1

sumt = -1
sum_expected = int(input("Input your expected sum of two nums (except for -1):"))

while front != rear:
    sumt = arr[front] + arr[rear]
    if sumt == sum_expected:
        # print(arr[front] + "+" + arr[rear] + "=" + sum_expected)
        print("%d + %d = %d" % (arr[front], arr[rear], sum_expected))
        break
    elif sumt > sum_expected:
        rear = rear - 1
    else:
        front = front + 1

if front == rear:
    print("There is no solution")
