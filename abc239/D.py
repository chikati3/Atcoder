a, b, c, d = map(int, input().split())

n = 10000
prime = [False] * (n+1)
prime[0] = True
prime[1] = True
pn = set()
for i in range(2, n+1):
    if prime[i] == False:
        pn.add(i)
        for j in range(i, n+1, i):
            prime[j] = True

for i in range(a, b+1):
    t = True
    for j in range(c, d+1):
        if i+j in pn:
            t = False
    if t == True:
        print('Takahashi')
        exit()
print('Aoki')