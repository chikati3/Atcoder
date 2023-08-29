n, k, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
for i in range(n):
    if x <= a[i] and 1 <= k:
        ki = a[i] // x
        if ki <= k:
            k -= ki
            a[i] = a[i] - ki * x
        else:
            a[i] = a[i] - k * x
            k = 0

a.sort(reverse=True)
for i in range(min(n, k)):
    a[i] = max(0, a[i] - x)
print(sum(a))