from heapq import heappop, heappush, heapify


n, k = map(int, input().split())
p = list(map(int, input().split()))

pq = p[:k]
heapify(pq)
print(pq[0])
for i in range(k, n):
    if pq[0] < p[i]:
        heappop(pq)
        heappush(pq, p[i])
    print(pq[0])