N = int(input())

x = []
for _ in range(N):
    t, l, r = map(int, input().split())
    if t == 1:
        x.append([l, r])
    elif t == 2:
        x.append([l, r-0.5])
    elif t == 3:
        x.append([l+0.5, r])
    elif t == 4:
        x.append([l+0.5, r-0.5])

cnt = 0
for i in range(N):
    a, b = x[i]
    for j in range(i+1, N):
        c, d = x[j]
        if d < a or b < c:
            cnt += 1
ans = N * (N - 1) // 2
print(ans - cnt)