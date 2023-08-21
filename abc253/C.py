from heapq import heappop, heappush


q = int(input())

mi = []
mx = []
cnt = {}
for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        heappush(mi, que[1])
        heappush(mx, -que[1])
        cnt.setdefault(que[1], 0)
        cnt[que[1]] += 1
    elif que[0] == 2 and que[1] in cnt:
        _, x, c = que
        cnt[x] = max(cnt[x] - c, 0)
    elif que[0] == 3:
        while cnt[mi[0]] == 0:
            heappop(mi)
        while cnt[-mx[0]] == 0:
            heappop(mx)
        print(-(mi[0] + mx[0]))
