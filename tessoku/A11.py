N, X = map(int, input().split())
A = list(map(int, input().split()))

A = [0] + A
left = 0
right = N
while right - left > 1:
    mid = (right + left) // 2
    if X <= A[mid]:
        right = mid
    else:
        left = mid
print(right)