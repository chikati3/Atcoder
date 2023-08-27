from bisect import bisect_left, bisect_right


n = int(input())
a = list(map(int, input().split()))

cnt = {}
for i in range(n):
    cnt.setdefault(a[i], [])
    cnt[a[i]].append(i)

q = int(input())
for _ in range(q):
    l, r, x = map(int,input().split())
    l -= 1
    r -= 1
    if x not in cnt:
        print(0)
    else:
        bl = bisect_left(cnt[x], l)
        br = bisect_right(cnt[x], r)
        print(br - bl)