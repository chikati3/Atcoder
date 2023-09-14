n, m  = map(int, input().split())
s = input().split()
t = input().split()

t = set(t)
for si in s:
    if si in t:
        print('Yes')
    else:
        print('No')