n, k = map(int, input().split())
a = list(map(int, input().split()))

# K未満になるループ回数
left = 0
right = max(a)
while right - left > 1:
    mid = (right + left) // 2
    x = 0
    for ai in a:
        x += min(ai, mid)
    if x < k:
        left = mid
    else:
        right = mid

for ai in a:
    k -= min(ai, left)

a = [max(0, ai - left) for ai in a]
for i in range(n):
    if k == 0:
        break
    elif 0 < a[i]:
        a[i] -= 1
        k -= 1
print(*a)