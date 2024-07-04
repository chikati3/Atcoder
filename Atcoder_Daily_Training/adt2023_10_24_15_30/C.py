P, Q = input().split()

x = 'ABCDEFG'
num = [3, 1, 4, 1, 5, 9]
p = x.index(P)
q = x.index(Q)
if q < p:
  p, q = q, p
print(sum(num[p:q]))