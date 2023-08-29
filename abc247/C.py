n = int(input())

ans = []
for i in range(1, n+1):
    ans = ans + [i] + ans
print(*ans)