S = input()

ans = ''
for si in S:
  if si not in 'aeiou':
    ans += si
print(ans)