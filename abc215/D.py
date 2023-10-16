N, M = map(int, input().split())
A = list(map(int, input().split()))

prime = [False] * (M+1)

x = set()
for a in A:
    s = set()
    while a % 2 == 0:
        s.add(2)
        a //= 2
    f = 3
    while f * f <= a:
        if a % f == 0:
            s.add(f)
            a //= f
        else:
            f += 2
    if a != 1:
        s.add(a)
    
    x |= s

for xi in x:
    for i in range(xi, M+1, xi):
        prime[i] = True
ans = []
for i in range(1, M+1):
    if prime[i] == False:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)