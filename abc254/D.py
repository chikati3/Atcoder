n = int(input())

cnt = [0] * (n+1)
for i in range(1, n+1):
    val = i
    j = 2
    while j*j <= val:
        if val % (j*j) == 0:
            val //= (j*j)
        else:
            j += 1
    cnt[val] += 1

ans = 0
for c in cnt:
    ans += c * c
print(ans)