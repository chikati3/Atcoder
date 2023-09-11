t = int(input())

for _ in range(t):
    a, s = map(int, input().split())
    x = s - 2*a
    if x & a == 0 and 0 <= x:
        print('Yes')
    else:
        print('No')