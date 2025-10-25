arr = [int(x) for x in input().split()]
ind = 0
for i in range(0, len(arr)):
    if arr[i] != 0:
        arr[ind] = arr[i]
        ind += 1
for i in range(ind, len(arr)):
    arr[i] = 0
print(arr)
