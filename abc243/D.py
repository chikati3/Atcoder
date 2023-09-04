n, x = map(int, input().split())
s = input()

x = list(bin(x)[2:])
for si in s:
    if si == 'U':
        x.pop()
    elif si == 'R':
        x.append('1')
    elif si == 'L':
        x.append('0')
x = ''.join(x)
print(int(x, 2))