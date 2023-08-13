s = input()
t = input()

sx = [['@', 0]]
for si in s:
    if sx[-1][0] == si:
        sx[-1][1] += 1
    else:
        sx.append([si, 1])
tx = [['@', 0]]
for ti in t:
    if tx[-1][0] == ti:
        tx[-1][1] += 1
    else:
        tx.append([ti, 1])
if len(sx) != len(tx):
    print('No')
else:
    for i in range(len(sx)):
        if sx[i][0] != tx[i][0]:
            print('No')
            exit()
        else:
            if sx[i][1] != tx[i][1]:
                if (sx[i][1] == 1 and 2 <= tx[i][1]) or sx[i][1] > tx[i][1]:
                    print('No')
                    exit()
    print('Yes')