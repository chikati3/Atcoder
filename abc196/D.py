H, W, A, B = map(int, input().split())

tatami = [[False] * W for _ in range(H)]
def dfs(i, j, a, b):
    if a < 0 or b < 0:
        return 0
    if j == W:
        j = 0
        i += 1
    if i == H:
        return 1
    if tatami[i][j] == True:
        return dfs(i, j+1, a, b)
    
    ans = 0
    tatami[i][j] = True
    ans += dfs(i, j+1, a, b-1)

    if j+1 < W and tatami[i][j+1] == False:
        tatami[i][j+1] = True
        ans += dfs(i, j+1, a-1, b)
        tatami[i][j+1] = False
    if i+1 < H and tatami[i+1][j] == False:
        tatami[i+1][j] = True
        ans += dfs(i, j+1, a-1, b)
        tatami[i+1][j] = False
    
    tatami[i][j] = False
    return ans

print(dfs(0, 0, A, B))