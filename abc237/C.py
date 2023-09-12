s = input()

l = 0
for si in s:
    if si == 'a':
        l += 1
    else:
        break
r = 0
for si in s[::-1]:
    if si == 'a':
        r += 1
    else:
        break
if r < l:
    print('No')
    exit()

s = 'a' * (r-l) + s
if s == s[::-1]:
    print('Yes')
else:
    print('No')