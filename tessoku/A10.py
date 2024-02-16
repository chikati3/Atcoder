N = int(input())
A = list(map(int, input().split()))
D = int(input())

left = [0] * (N+1)
right = [0] * (N+1)
for i in range(1, N+1):
    left[i] = max(left[i-1], A[i-1])

    n = N-i
    right[n] = max(right[n+1], A[n])

for _ in range(D):
    L, R = map(int, input().split())
    l, r = L-1, R-N-1
    print(max(left[l], right[r]))