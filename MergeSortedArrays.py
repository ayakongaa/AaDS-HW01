arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

ptr1 = len(arr1) - 1
arr1 += [0] * len(arr2)
ptr2 = len(arr2) - 1
ptr3 = len(arr1) - 1

while (ptr2 >= 0):
    if (arr1[ptr1] > arr2[ptr2] and ptr1 >= 0):
        arr1[ptr3] = arr1[ptr1]
        ptr1 -= 1
    else:
        arr1[ptr3] = arr2[ptr2]
        ptr2 -= 1
    ptr3 -= 1
print(arr1)
