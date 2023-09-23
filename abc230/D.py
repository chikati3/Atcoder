N, D = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(N)]

LR = sorted(LR, key=lambda x : x[1])
ans = 0
p = 0
for i in range(N):
    L, R = LR[i]
    if p < L:
        ans += 1
        p = R + D - 1
print(ans)