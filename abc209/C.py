N = int(input())
C = list(map(int, input().split()))

C.sort()
mod = 10**9+7

ans = C[0]
for i in range(1, N):
    ans *= max(0, C[i] - i)
    ans %= mod
print(ans)