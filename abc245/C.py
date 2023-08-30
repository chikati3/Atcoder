n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

lis = [[False, False] for _ in range(n)]
lis[0] = [True, True]

for i in range(n-1):
    if abs(a[i] - a[i+1]) <= k:
        lis[i+1][0] |= lis[i][0]
    if abs(b[i] - a[i+1]) <= k:
        lis[i+1][0] |= lis[i][1]
    if abs(a[i] - b[i+1]) <= k:
        lis[i+1][1] |= lis[i][0]
    if abs(b[i] - b[i+1]) <= k:
        lis[i+1][1] |= lis[i][1]

if lis[-1][0] or lis[-1][1]:
    print('Yes')
else:
    print('No')