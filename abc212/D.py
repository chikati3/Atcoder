from heapq import heappop, heappush


Q = int(input())

pq = []
s = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heappush(pq, q[1] - s)
    elif q[0] == 2:
        s += q[1]
    elif q[0] == 3:
        print(heappop(pq) + s)