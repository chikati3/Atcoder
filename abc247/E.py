n, x, y = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
l = [-1] * 3
for i in range(n):
    if a[i] == x:
        l[1] = i
    if a[i] == y:
        l[2] = i
    if a[i] < y or x < a[i]:
        l[0] = i
    if l[1] != -1 and l[2] != -1:
        ans += max(0, min(l[1], l[2]) - l[0])
print(ans)