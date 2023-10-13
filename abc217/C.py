N = int(input())
P = list(map(int, input().split()))

p = []
for i in range(N):
    p.append([P[i], i+1])
p.sort()

ans = []
for _, pi in p:
    ans.append(pi)
print(*ans)