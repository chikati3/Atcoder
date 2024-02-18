N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
l = 0
for i in range(N):
    left = i
    right = N
    while right - left > 1:
        mid = (right + left) // 2
        if K < A[mid] - A[i]:
            right = mid
        else:
            left = mid
    n = (right - i)
    ans += n * (n - 1) // 2
    ans -= l * (l - 1) // 2
    l = right - i - 1
print(ans)