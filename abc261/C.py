n = int(input())

d = {}
for _ in range(n):
    s = input()
    if s not in d:
        print(s)
        d[s] = 0
    else:
        d[s] += 1
        print(s + '(' + str(d[s]) + ')')