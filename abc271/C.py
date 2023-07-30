from collections import deque


n = int(input())
a = list(map(int, input().split()))

a.sort()
d = deque()
s = set()
cnt = 0
for i in range(n):
    if a[i] not in s:
        d.append(a[i])
        s.add(a[i])
    else:
        cnt += 1

nxt = 0
while d or 2 <= cnt:
    if 1 <= len(d) and nxt+1 == d[0]:
        d.popleft()
    elif 2 <= cnt:
        cnt -= 2
    elif 1 <= len(d) and 1 <= cnt:
        d.pop()
        cnt -= 1
    elif 2 <= len(d):
        d.pop()
        d.pop()
    else:
        break
    nxt += 1
print(nxt)