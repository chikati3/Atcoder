
from collections import deque


q = int(input())
mod = 998244353

d = deque()
d.append(1)
ans = 1
for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        d.append(que[1])
        ans = ans * 10 + que[1]
        ans %= mod
    elif que[0] == 2:
        x = d.popleft()
        ans = ans - (x * pow(10, len(d), mod))
        ans %= mod
    else:
        print(ans)