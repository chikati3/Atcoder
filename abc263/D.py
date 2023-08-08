n, l, r = map(int, input().split())
a = list(map(int, input().split()))

left = [0]
for i in range(n):
    left.append(min(left[-1]+a[i], l*(i+1)))

ar = a[::-1]
right = [0]
for i in range(n):
    right.append(min(right[-1]+ar[i], r*(i+1)))
right = right[::-1]

ans = 10**20
for i in range(n+1):
    ans = min(ans, left[i] + right[i])
print(ans)