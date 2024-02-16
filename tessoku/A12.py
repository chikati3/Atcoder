N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

left = 0
right = 10**10
while right - left > 1:
    mid = (right + left) // 2
    cnt = 0
    for i in range(N):
        cnt += mid // A[i]
    if K <= cnt:
        right = mid
    else:
        left = mid
print(right)