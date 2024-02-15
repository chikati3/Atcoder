D = int(input())
N = int(input())

day = [0] * (D+10)
for _ in range(N):
    L, R = map(int, input().split())
    R += 1
    day[L] += 1
    day[R] -= 1

now = 0
for i in range(1, D+1):
    now += day[i]
    print(now)