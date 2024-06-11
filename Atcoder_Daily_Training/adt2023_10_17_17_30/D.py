N, A, B = map(int, input().split())

x = '.' * B + '#' * B
y = '#' * B + '.' * B

x *= 100
y *= 100

flip = 0
for i in range(N):
  for j in range(A):
    if flip == 0:
      print(x[:N*B])
    else:
      print(y[:N*B])
  flip = 1 - flip