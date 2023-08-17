h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
n = 30
for i in range(1, n+1):
    if h1 <= i:
        continue
    for j in range(1, n+1):
        if h1 <= i+j:
            continue
        for k in range(1, n+1):
            if h2 <= k:
                continue
            for v in range(1, n+1):
                if h2 <= k+v:
                    continue
                elif 1 <= w1-i-k and 1 <= w2-j-v and 1 <= h3-(w1-i-k)-(w2-j-v):
                    if w3 == h1-i-j + h2-k-v + h3-(w1-i-k)-(w2-j-v):

                        ans += 1
print(ans)