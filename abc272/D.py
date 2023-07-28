from collections import deque


n, m = map(int, input().split())

field= [[-1]*n for _ in range(n)]
field[0][0] = 0

yx = []
mm = int(m**0.5) + 1
for i in range(-mm, mm+1):
    for j in range(-mm, mm+1):
        if i**2 + j**2 == m:
            yx.append((i, j))

d = deque()
d.append((0, 0))
while d:
    y, x = d.popleft()
    for dy, dx in yx:
        if 0 <= y+dy < n and 0 <= x+dx < n:
            if field[y+dy][x+dx] == -1:
                field[y+dy][x+dx] = field[y][x] + 1
                d.append((y+dy, x+dx))

for i in field:
    print(*i)