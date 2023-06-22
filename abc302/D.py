
from bisect import bisect_left, bisect_right


n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
ans = -1
for ai in a:
    # 差がd以下を探す
    l = bisect_left(b, ai - d) - 1
    r = bisect_right(b, ai + d) - 1

    if abs(ai - b[l]) <= d:
        ans = max(ans, ai + b[l])
    if abs(ai - b[r]) <= d:
        ans = max(ans, ai + b[r])
print(ans)
