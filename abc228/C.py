from bisect import bisect_right


N, K = map(int, input().split())

p = []
for _ in range(N):
    pi = list(map(int, input().split()))
    p.append(sum(pi))

score = p[:]
score.sort()

for i in range(N):
    b = bisect_right(score, p[i] + 300)
    if N - K + 1 <= b:
        print('Yes')
    else:
        print('No')