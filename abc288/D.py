#pypy3
# 不変量
# i mod Kの累積和

n, k = map(int, input().split())
a = list(map(int, input().split()))
q = int(input())

s = [[0] for _ in range(k)]
for i in range(n):
    s[i%k].append(s[i%k][-1] + a[i])

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    x = []
    for i in range(k):
        li, ri = (l-i+k-1)//k, (r-i+k-1)//k
        if li != ri:
            x.append(s[i][ri] - s[i][li])
    
    if all(x[j] == x[0] for j in range(len(x))):
        print('Yes')
    else:
        print('No')