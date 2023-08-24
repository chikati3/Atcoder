n = int(input())

prime = [False] * (10**6+1)
prime[0] = True
prime[1] = True
p = []
for i in range(10**6+1):
    if prime[i] == False:
        p.append(i)
        for j in range(i, 10**6+1, i):
            prime[j] = True

ans = 0
for i in range(1, len(p)):
    a = p[i] ** 3
    if n < a:
        break
    
    l = -1
    r = i
    while r - l > 1:
        mid = (r + l) // 2
        if n < a * p[mid]:
            r = mid
        else:
            l = mid
    ans += l+1
print(ans)