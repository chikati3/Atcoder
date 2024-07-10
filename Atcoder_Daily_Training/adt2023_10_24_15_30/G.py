S = input()

N = len(S)
box = set()
x = []
l = 0
for s in S:
  if s == '(':
    l += 1
    x.append(s)
  elif s == ')':
    if 1 <= l:
      while 1 <= l:
        y = x.pop()
        if y == ')':
          print('No')
          exit()
        elif y == '(':
          l -= 1
          break
        else:
          box.discard(y)
    else:
      print('No')
      exit()
  else:
    if s in box:
      print('No')
      exit()
    else:
      box.add(s)
      x.append(s)
print('Yes')