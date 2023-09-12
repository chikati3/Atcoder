from collections import deque


n = int(input())
s = input()

d = deque()
d.append(n)
for i in range(n-1, -1, -1):
    if s[i] == 'L':
        d.append(i)
    else:
        d.appendleft(i)
print(*d)