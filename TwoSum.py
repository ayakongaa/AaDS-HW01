arr = [int(x) for x in input().split()]
target = int(input())
left = 0
right = len(arr) - 1
while (left < right):
    s = arr[left] + arr[right]
    if (s == target):
        break
    elif (s < target):
        left += 1
    else:
        right -= 1        
print(left, right)
