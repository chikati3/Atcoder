n = int(input())

bit = bin(n)[2:]
idx = []
for i in range(len(bit)-1, -1, -1):
    if bit[i] == '1':
        idx.append(i)

ans = set()
for i in range(2**len(idx)):
    x = ['0'] * len(bit)
    for j in range(len(idx)):
        if i >> j & 1:
            x[idx[j]] = '1'
    ans.add(int(''.join(x), 2))
ans = sorted(ans)
for i in ans:
    print(i)