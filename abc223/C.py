N = int(input())

t = 0
ab = []
for _ in range(N):
    A, B = map(int, input().split())
    t += A / B
    ab.append((A, B))
t /= 2

ans = 0
for a, b in ab:
    if a / b <= t:
        ans += a
        t -= a / b
    else:
        ans += b * t
        break
print(ans)