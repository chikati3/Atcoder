from collections import deque


q = int(input())

d = deque()
for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        _, x, c = que
        d.append([x, c])
    else:
        _, c = que
        ans = 0
        while 1 <= len(d) and d[0][1] <= c:
            xi, ci = d.popleft()
            ans += xi * ci
            c -= ci
        if 1 <= len(d) and c != 0:
            xi, ci = d.popleft()
            ans += xi * c
            d.appendleft([xi, ci-c])
        print(ans)