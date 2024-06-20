N = int(input())
P = list(map(int, input().split()))

P = [0, 0] + P
now = N
cnt = 0
while now != 1:
  now = P[now]
  cnt += 1
print(cnt)