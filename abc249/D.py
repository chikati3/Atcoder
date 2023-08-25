n = int(input())
a = list(map(int, input().split()))

num = 2*10**5+1
x = [0] * num
for ai in a:
    x[ai] += 1

ans = 0
for i in range(1, num):
    j = 1
    while i*j < num:
        ans += x[i] * x[j] * x[i*j]
        j += 1
print(ans)