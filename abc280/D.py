def prime_factorize(n):
  a = []
  while n % 2 == 0:
    a.append(2)
    n //= 2
  f = 3
  while f * f <= n:
    if n % f == 0:
      a.append(f)
      n //= f
    else:
      f += 2
  if n != 1:
    a.append(n)
  return a

k = int(input())
prime = prime_factorize(k)
cnt = {}
for pi in prime:
  cnt.setdefault(pi, 0)
  cnt[pi] += 1

ans = 0
for i in cnt:
  for j in range(1, 10**6):
    num = i * j
    while num % i == 0:
      num //= i
      cnt[i] -= 1
    if cnt[i] <= 0:
      ans = max(ans, i * j)
      break
print(ans)