num = 10**7
p = [False] * (num+1)
prime = []
for i in range(2, num):
    if p[i] == False:
      p[i] = True
      prime.append(i)
      for j in range(i+i, num, i):
          p[j] = True

t = int(input())
for _ in range(t):
   n = int(input())
   for i in prime:
      if n % (i*i) == 0:
         print(i, n//(i*i))
         break
      elif n % i == 0:
         print(int((n//i)**0.5), i)
         break