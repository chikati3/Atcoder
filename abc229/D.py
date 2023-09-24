S = input()
K = int(input())

N = len(S)

l = 0
x = 0
ng = 0
ans = 0
for r in range(N):
    if S[r] == 'X':
        x += 1
    else:
        ng += 1
    while K < ng and l <= r:
        if S[l] == 'X':
            x -= 1
        else:
            ng -= 1
        l += 1
    ans = max(ans, x + ng)
print(ans)