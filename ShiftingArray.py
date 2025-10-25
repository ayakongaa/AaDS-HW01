def reverseArr(arr, l, r):
    while (l <  r):
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr

arr = [int(x) for x in input().split()]
k = int(input())
k = k % (len(arr) - 1)

reverseArr(arr, 0, len(arr) - 1)
reverseArr(arr, 0, k - 1)
reverseArr(arr, k, len(arr) - 1)

print(arr)
