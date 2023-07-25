from collections import deque


h, w = map(int, input().split())
c = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == 'S':
            sy, sx = i, j
            break

ans = 'No'

xy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for dy, dx in xy:
    ny, nx = sy+dy, sx+dx
    if 0 <= ny < h and 0 <= nx < w and c[ny][nx] == '.':
        d = deque()
        d.append((ny, nx))
        dist = [[-1]*w for _ in range(h)]
        dist[ny][nx] = 1
        while d:
            y, x = d.popleft()
            for dy, dx in xy:
                if 0 <= y+dy < h and 0 <= x+dx < w:
                    if dist[y+dy][x+dx] == -1:
                        if c[y+dy][x+dx] == '.':
                            dist[y+dy][x+dx] = dist[y][x] + 1
                            d.append((y+dy, x+dx))
                        elif c[y+dy][x+dx] == 'S' and 4 <= dist[y][x]+1:
                            ans = 'Yes'
print(ans)