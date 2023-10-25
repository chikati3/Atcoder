from collections import defaultdict


N, K = map(int, input().split())
C = list(map(int, input().split()))

cnt = defaultdict(int)
ans = 0
for i in range(K):
    cnt[C[i]] += 1
    if cnt[C[i]] == 1:
        ans += 1

c = len(cnt)
for i in range(N-K):
    cnt[C[i]] -= 1
    if cnt[C[i]] == 0:
        c -= 1
    
    cnt[C[i+K]] += 1
    if cnt[C[i+K]] == 1:
        c += 1
    ans = max(ans, c)
print(ans)