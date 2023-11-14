N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cnt = {}
for i in range(N):
    b = B[C[i]-1]
    cnt.setdefault(b, 0)
    cnt[b] += 1

ans = 0
for i in range(N):
    if cnt.get(A[i]):
        ans += cnt[A[i]]
print(ans)