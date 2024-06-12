N = int(input())
S = input()

left = 0
ans = []
for i in range(N):
  ans.append(S[i])
  if ans[-1] == '(':
    left += 1
  
  if ans[-1] == ')' and 1 <= left:
    while True:
      x = ans.pop()
      if x == '(':
        left -= 1
        break
print(''.join(ans))