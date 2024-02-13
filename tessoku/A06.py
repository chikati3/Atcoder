N, Q = map(int, input().split())
A = list(map(int, input().split()))

day = [0]
for i in range(N):
    day.append(day[-1] + A[i])

for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    print(day[R] - day[L])