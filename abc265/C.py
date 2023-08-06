h, w = map(int, input().split())
g = [input() for _ in range(h)]

visited = [[False]*w for _ in range(h)]
visited[0][0] = True
y, x = 0, 0
ans = [[1, 1]]
for i in range(h*w):
    if g[y][x] == 'U':
        y -= 1
    elif g[y][x] == 'D':
        y += 1
    elif g[y][x] == 'L':
        x -= 1
    elif g[y][x] == 'R':
        x += 1
    
    if 0 <= y < h and 0 <= x < w:
        if visited[y][x] == False:
            visited[y][x] = True
            ans.append([y+1, x+1])
        else:
            print(-1)
            exit()
    else:
        break
print(*ans[-1])