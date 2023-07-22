from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
q = int(input())

d = defaultdict(int)
num_all = -1
for _ in range(q):
    que = list(map(int, input().split()))
    if num_all == -1:
        if que[0] == 1:
            num_all = que[1]
        elif que[0] == 2:
            _, x, y = que
            x -= 1
            a[x] += y
        elif que[0] == 3:
            _, x = que
            x -= 1
            print(a[x])
    else:
        if que[0] == 1:
            num_all = que[1]
            d = defaultdict(int)
        elif que[0] == 2:
            _, x, y = que
            x -= 1
            d[x] += y
        else:
            _, x = que
            x -= 1
            print(num_all + d[x])