from collections import deque


n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
s = [input() for _ in range(n)]

ax -= 1
ay -= 1
bx -= 1
by -= 1 
d = deque()
d.append([ax, ay])
dist = [[-1]*n for _ in range(n)]
dist[ax][ay] = 0
while d:
    xi, yi = d.popleft()
    for dx in [-1, 1]:
        for dy in [-1, 1]:
            x = xi + dx
            y = yi + dy
            while True:
                if x < 0 or n <= x or y < 0 or n <= y:
                    break
                if s[x][y] == '#':
                    break
                if dist[x][y] != -1 and dist[x][y] <= dist[xi][yi]:
                    break
                if dist[x][y] < dist[xi][yi]:
                    dist[x][y] = dist[xi][yi] + 1
                    d.append([x, y])
                x += dx
                y += dy
print(dist[bx][by])