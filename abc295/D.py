
s = input()
n = len(s)

d = {}
bit = 0
d[bit] = 1
for i in range(n):
    bit ^= 2 ** int(s[i])
    d.setdefault(bit, 0)
    d[bit] += 1
ans = 0
for di in d:
    v = d[di]
    ans += v * (v-1) // 2
print(ans)