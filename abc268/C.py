n = int(input())
p = list(map(int, input().split()))

cnt = [0] * n
for i in range(n):
    idx = (p[i] - i) % n
    cnt[(idx-1) % n] += 1
    cnt[idx] += 1
    cnt[(idx+1) % n] += 1
print(max(cnt))