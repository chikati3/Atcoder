n, k = map(int, input().split())
s = [input() for _ in range(n)]

ans = 0
for i in range(2**n):
    cnt = [0] * 26
    for j in range(n):
        if i >> j & 1:
            for si in s[j]:
                cnt[ord(si) - 97] += 1
    ans = max(ans, cnt.count(k))
print(ans)