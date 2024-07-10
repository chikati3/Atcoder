N = int(input())
A = list(map(int, input().split()))

pizza = [0] * (360+1)
pizza[0] = 1
cut = 0
for i in range(N):
  cut += A[i]
  cut %= 360
  pizza[cut] = 1

cuts = []
for i in range(360+1):
  if pizza[i] == 1:
    cuts.append(i)
cuts.append(360)

ans = 0
for i in range(len(cuts)-1):
  ans = max(ans, cuts[i+1] - cuts[i])
print(ans)