from collections import deque
from bisect import bisect_left


x = int(input())

num = set(range(1, 100))
d = deque()
for i in range(10, 100):
    d.append(i)

while d:
    y = d.popleft()

    if y <= 10**18:
        diff = y//10%10 - y%10
        if 0 <= y%10 + diff <= 9:
            ny = y*10 + (y%10 + diff)
            if diff == ny//10%10 - ny%10:
                if ny not in num:
                    d.append(ny)
                    num.add(ny)
        if 0 <= y%10 - diff <= 9:
            ny = y*10 + (y%10 - diff)
            if diff == ny//10%10 - ny%10:
                if ny not in num:
                    d.append(ny)
                    num.add(ny)
num = sorted(num)
b = bisect_left(num, x)
print(num[b])