arr = [int(x) for x in input().split()]
chet = 0
n = len(arr)
for i in range(0, n):
    if arr[i] % 2 == 0:
        arr[i], arr[chet] = arr[chet], arr[i]
        chet += 1
print(arr)
