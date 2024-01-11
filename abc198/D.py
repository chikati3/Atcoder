from itertools import permutations


s1 = input()
s2 = input()
s3 = input()

if 10 < len(set(s1 + s2 + s3)):
    print('UNSOLVABLE')
    exit()

s = list(set(s1 + s2 + s3))
n = len(s)

def num(l):
    x = 0
    for i in range(len(l)):
        x += d[l[i]] * 10 **(len(l)-i-1)
    return x

for it in permutations(list(range(10)), n):
    d = {}
    for i in range(n):
        d[s[i]] = it[i]
    if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
        continue
    
    t1 = num(s1)
    t2 = num(s2)
    t3 = num(s3)
    if t1 + t2 == t3:
        print(t1)
        print(t2)
        print(t3)
        exit()

print('UNSOLVABLE')