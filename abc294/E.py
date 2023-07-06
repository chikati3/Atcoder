l, n1, n2 = map(int, input().split())
vl1 = [list(map(int, input().split())) for _ in range(n1)]
vl2 = [list(map(int, input().split())) for _ in range(n2)]

i1 = 0
i2 = 0
r1 = 0
r2 = 0

ans = 0
while i1 < n1 and i2 < n2:
    if vl1[i1][0] == vl2[i2][0]:
        ans += min(vl1[i1][1] + r1, vl2[i2][1] + r2) - max(r1, r2)
    
    if vl1[i1][1] + r1 < vl2[i2][1] + r2:
        r1 += vl1[i1][1]
        i1 += 1
    else:
        r2 += vl2[i2][1]
        i2 += 1
print(ans)