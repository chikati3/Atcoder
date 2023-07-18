s = input()

box = set()
x = []
for si in s:
    if si == '(':
        x.append(si)
    elif si == ')':
        while True:
            y = x.pop()
            if y == '(':
                break
            box.discard(y)
    else:
        if si not in box:
            box.add(si)
        else:
            print('No')
            exit()
        x.append(si)
print('Yes')