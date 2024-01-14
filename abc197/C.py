N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for i in range(2**N):
    OR = 0
    XOR = 0
    for j in range(N):
        if i >> j & 1:
            OR |= A[j]
        else:
            XOR ^= OR
            OR = A[j]
    XOR ^= OR
    ans = min(ans, XOR)
print(ans)