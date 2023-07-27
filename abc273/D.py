from bisect import bisect_left


h, w, r, c = map(int, input().split())
n = int(input())

hight = {}
width = {}
hi = set()
wi = set()
for _ in range(n):
    x, y = map(int, input().split())
    hight.setdefault(y, [])
    width.setdefault(x, [])
    hight[y].append(x)
    width[x].append(y)
    hi.add(y)
    wi.add(x)

for v in hight:
    hight[v].sort()
for v in width:
    width[v].sort()

q = int(input())
x, y = r, c
for _ in range(q):
    d, l = input().split()
    l = int(l)

    if d == 'U':
        if y not in hi:
            x -= l
        else:
            idx = bisect_left(hight[y], x) - 1
            if idx == -1:
                x -= l
            else:
                x = max(x-l, hight[y][idx] + 1)
    elif d == 'D':
        if y not in hi:
            x += l
        else:
            idx = bisect_left(hight[y], x)
            if idx == len(hight[y]):
                x += l
            else:
                x = min(x+l, hight[y][idx]-1)
    elif d == 'L':
        if x not in wi:
            y -= l
        else:
            idx = bisect_left(width[x], y) - 1
            if idx == -1:
                y -= l
            else:
                y = max(y-l, width[x][idx]+1)
    elif d == 'R':
        if x not in wi:
            y += l
        else:
            idx = bisect_left(width[x], y)
            if idx == len(width[x]):
                y += l
            else:
                y = min(y+l, width[x][idx]-1)
    x = max(1, min(x, h))
    y = max(1, min(y, w))
    print(x, y)