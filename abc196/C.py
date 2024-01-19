N = int(input())

ans = 0
for i in range(1, N+1):
    x = int(str(i) + str(i))
    if x <= N:
        ans += 1
    else:
        break
print(ans)