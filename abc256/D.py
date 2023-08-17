n = int(input())

num = 2*10**5+10
a = [0] * (num+1)
for _ in range(n):
    x, y = map(int, input().split())
    a[x] += 1
    a[y] -= 1

for i in range(num-1):
    a[i+1] += a[i]

l = 0
for i in range(num+1):
    if 0 == l and 1 <= a[i]:
        l = i
    elif 1 <= l and a[i] == 0:
        print(l, i)
        l = 0