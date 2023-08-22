n = int(input())

cnt = [set() for _ in range(10)]
for _ in range(n):
    s = input()
    for i in range(10):
        si  = int(s[i])
        t = i
        while t in cnt[si]:
            t += 10
        cnt[si].add(t)

ans = float('inf')
for i in cnt:
    i = sorted(i)
    ans = min(ans, max(i))
print(ans)