K = int(input())
A, B = input().split()

def f(x):
  num = 0
  n = len(x)
  for i in range(n):
    num += int(x[i]) * K ** (n-i-1)
  return num

print(f(A) * f(B))