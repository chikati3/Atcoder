n = int(input())
a = list(map(int, input().split()))

a = [i-1 for i in a]

x, y = 0, 0
for i in range(n):
    if i == a[i]:
        x += 1
    elif i == a[a[i]]:
        y += 1

def f(n):
    return n * (n-1) // 2

print(f(x) + y//2)