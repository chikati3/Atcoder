N, Q = map(int, input().split())
A = list(map(int, input().split()))

A = [0] + A + [10**20]

for _ in range(Q):
    k = int(input())
    left = 0
    right = N + 1
    while right - left > 1:
        mid = (right + left) // 2
        if A[mid] < k + mid:
            left = mid
        else:
            right = mid
    print(k + left)