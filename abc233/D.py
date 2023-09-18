n, k = map(int, input().split())
a = list(map(int, input().split()))

acc = [0]
for ai in a:
    acc.append(acc[-1] + ai)

cnt = {}
cnt[0] = 1
ans = 0
for i in range(1, n+1):
    x = acc[i] - k
    if x in cnt:
        ans += cnt[x]
    cnt.setdefault(acc[i], 0)
    cnt[acc[i]] += 1
print(ans)