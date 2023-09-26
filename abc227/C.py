N = int(input())

ans = 0
for a in range(1, N+1):
    if N < a*a*a:
        break
    for b in range(a, N+1):
        if N < a*b*b:
            break
        ans += max(0, N//a//b - b + 1)
print(ans)