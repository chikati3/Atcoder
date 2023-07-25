n = int(input())
a = list(map(int, input().split()))

cnt2 = []
cnt3 = []
x = []
for ai in a:
    c2 = 0
    c3 = 0
    while ai % 2 == 0:
        c2 += 1
        ai //= 2
    while ai % 3 == 0:
        c3 += 1
        ai //= 3
    cnt2.append(c2)
    cnt3.append(c3)
    x.append(ai)
x.sort()

if x[0] == x[-1]:
    ans = 0
    ans += sum(cnt2) - min(cnt2) * n
    ans += sum(cnt3) - min(cnt3) * n
else:
    ans = -1
print(ans)