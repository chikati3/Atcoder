n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

cum = [0]
for ai in a:
    cum.append(cum[-1] + ai)

s = set(cum)
for i in range(n+1):
    pi = p + cum[i]
    qi = q + pi
    ri = r + qi
    if pi in s and qi in s and ri in s:
        print('Yes')
        exit()
print('No')