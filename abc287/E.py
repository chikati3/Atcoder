n = int(input())

s = []
for i in range(n):
    si = input()
    s.append((si, i))
s.sort()

def f(x1, x2):
    cnt = 0
    for i, j in zip(x1, x2):
        if i == j:
            cnt += 1
        else:
            break
    return cnt

ans = [0] * (n+1)
for i in range(n-1):
    l = f(s[i-1][0], s[i][0])
    r = f(s[i][0], s[i+1][0])
    ans[s[i][1]] = max(l, r)
ans[s[-1][1]] = f(s[-2][0], s[-1][0])

for i in range(n):
    print(ans[i])