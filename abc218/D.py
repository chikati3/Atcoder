N = int(input())
xy = set(tuple(map(int, input().split())) for _ in range(N))

ans = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        if y1 < y2 and x1 < x2:
            if (x1, y2) in xy and (x2, y1) in xy:
                ans += 1
print(ans)