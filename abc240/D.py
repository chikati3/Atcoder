n = int(input())
a = list(map(int, input().split()))

x = [[0, 0]]
ans = 0
for i in range(n):
    if x[-1][0] == 0 or x[-1][0] != a[i]:
        ans += 1
        x.append([a[i], 1])
    elif x[-1][0] == x[-1][1] + 1:
        ans -= x[-1][1]
        x.pop()
    else:
        ans += 1
        x[-1][1] += 1
    print(ans)