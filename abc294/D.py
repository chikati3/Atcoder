from heapq import heappop, heappush


n, q = map(int, input().split())

pq = list(range(1, n+1))
s = []
v = set()
for _ in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        p = heappop(pq)
        heappush(s, p)
    elif event[0] == 2:
        v.add(event[1])
    elif event[0] == 3:
        while s[0] in v:
            heappop(s)
        print(s[0])