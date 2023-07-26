n, x, y = map(int, input().split())
a = list(map(int, input().split()))

odd = a[::2]
even = a[1::2]

def f(lis, st):
    for i in lis:
        s = set()
        for j in st:
            s.add(j-i)
            s.add(j+i)
        st = s
    return st

s1 = set()
s1.add(odd[0])

s2 = set()
s2.add(even[0])
s2.add(-even[0])

s1 = f(odd[1:], s1)
s2 = f(even[1:], s2)
if y in s2 and x in s1:
    print('Yes')
else:
    print('No')