
n = int(input())

left = 1
right = n
while right - left > 1:
    mid = (right + left) // 2
    print('?', mid)
    s = int(input())
    if s == 0:
        left = mid
    else:
        right = mid
print('!', left)