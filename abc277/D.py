n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
num = sum(a)

x = [[a[0]]]
idx = 0
for i in range(1, n):
    if x[idx][-1] == a[i] or x[idx][-1]+1 == a[i]:
        x[idx].append(a[i])
    else:
        x.append([])
        idx += 1
        x[idx].append(a[i])

if 2 <= len(x) and (a[0] == a[-1] % m or (a[-1] + 1) % m == a[0]):
    x[-1] += x[0]

ans = 10**20
for i in range(len(x)):
    ans = min(ans, num - sum(x[i]))
print(ans)