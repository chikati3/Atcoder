N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

time = 0
for a, b in AB:
  time += a / b
time /= 2

ans = 0
for a, b in AB:
  if 0 <  time - a/b:
    time -= a/b
    ans += a
  else:
    ans += time * b
    break
print(ans)