x, a, d, n = map(int, input().split())

if d < 0:
    x = -x
    a = -a
    d = -d

left = 0
right = n-1
while right - left > 1:
    mid = (right + left) // 2
    if d * mid+ a <= x:
        left = mid
    else:
        right = mid
    
l = a + (left * d)
r = a + (left+1) * d
if left == n:
    print(abs(l - d - x))
else:
    print(min(abs(l-x), abs(r-x)))