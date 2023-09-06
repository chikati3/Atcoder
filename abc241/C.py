n = int(input())
s = [input() for _ in range(n)]

xy = [[0, 1], [1, 0], [1, 1], [1, -1]]
ans = 'No'
for i in range(n):
    for j in range(n):
        for x, y in xy:
            cnt = 0
            if s[i][j] == '#':
                cnt += 1
            ny, nx = i, j
            if 0 <= i + 5*y < n and 0 <= j + 5*x < n:
                for _ in range(5):
                    ny += y
                    nx += x
                    if s[ny][nx] == '#':
                        cnt += 1
                if 4 <= cnt:
                    ans = 'Yes'
print(ans)