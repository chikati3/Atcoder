n = int(input())

xy = []
p = []
for _ in range(n):
    x, y, pi = map(int, input().split())
    xy.append([x, y])
    p.append(pi)

INF = 1 << 30
def judge(s):
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            xi, yi = xy[i]
            xj, yj = xy[j]
            if p[i] * s >= abs(xi - xj) + abs(yi - yj):
                dist[i][j] = 1
    # ワーシャルフロイド法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    for i in range(n):
        if dist[i].count(INF) == 0:
            return True
    return False
# 二分探索
left = 0
right = 1 << 32
while right - left > 1:
    mid = (right + left) >> 1
    if judge(mid):
        right = mid
    else:
        left = mid
print(right)