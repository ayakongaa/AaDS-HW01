arr = [int(x) for x in input().split()]
mid = len(arr) // 2
for i in range(0, mid):
    tmp = arr[i]
    arr[i] = arr[len(arr) - 1 - i] 
    arr[len(arr) - 1 - i] = tmp
print(arr)
