# バブルソート

s = list(input())

x = 'atcoder'
idx = [x.index(s[i]) for i in range(len(s))]

ans = 0
while True:
    cnt = 0
    for i in range(len(s)-1):
        if idx[i] > idx[i+1]:
            idx[i], idx[i+1] = idx[i+1], idx[i]
            ans += 1
            cnt += 1
    if cnt == 0:
        break
print(ans)