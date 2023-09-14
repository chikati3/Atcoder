n = int(input())

a = [[0] * (2*n) for _ in range(2*n)]
for i in range(2*n-1):
    a[i][i+1:] = map(int, input().split())

ans = 0
used = [0] * (2*n)

def dfs(score):
    global ans, used
    for i in range(2*n):
        if used[i] == 0:
            used[i] = 1
            l = i
            break
    else:
        ans = max(ans, score)
        return
    
    for i in range(i+1, 2*n):
        if used[i] == 0:
            used[i] = 1
            dfs(score ^ a[l][i])
            used[i] = 0
    used[l] = 0
dfs(0)
print(ans)