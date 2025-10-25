arr = [int(x) for x in input().split()]
l = 0
r = len(arr) - 1
while (l < r):
    while arr[l] != 1 and l < r:
        l += 1
    while arr[r] != 0 and l < r:
        r -= 1
    if arr[l] > arr[r]:
        arr[l], arr[r] = arr[r], arr[l]
        r -= 1
        l += 1
print(arr)
