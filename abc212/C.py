from bisect import bisect_left


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B = sorted(set(B))
m = len(B)

ans = float('inf')
for ai in A:
    b = bisect_left(B, ai)
    ans = min(ans, abs(B[b-1] - ai), abs(B[b%m] - ai))
print(ans)