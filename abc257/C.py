n = int(input())
s = input()
w = list(map(int, input().split()))

ws = []
for i in range(n):
    ws.append([w[i], s[i]])
ws.sort()
ws.append([-1, '-1'])

zero = 0
one = abs(n - s.count('0'))
ans = one
for i in range(n):
    if ws[i][1] == '1':
        one -= 1
    elif ws[i][1] == '0':
        one += 1
    if ws[i][0] == ws[i+1][0]:
        continue
    ans = max(ans, zero + one)
print(ans)