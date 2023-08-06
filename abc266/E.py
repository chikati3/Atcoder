n = int(input())

ans = [0]
c = 0
for i in range(n):
    c = 0
    for j in range(1, 6+1):
        c += max(ans[-1], j)
    c /= 6
    ans.append(c)
print(ans[-1])