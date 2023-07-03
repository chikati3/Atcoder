
from heapq import heappop, heappush


n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []
pq = [0]
s = set()
while len(ans) < k+1:
    p = heappop(pq)
    ans.append(p)
    for ai in a:
        if p + ai not in s:
            s.add(p + ai)
            heappush(pq, p + ai)
print(ans[k])