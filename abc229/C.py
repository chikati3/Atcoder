N, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(reverse=True)
ans = 0
for A, B in AB:
    if B <= W:
        ans += A * B
        W -= B
    else:
        ans += A * W
        break
print(ans)