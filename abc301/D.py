

s = input()
n = int(input())

s_zero = s.replace('?', '0')
ans = list(s_zero)

for i in range(len(s)):
    if s[i] == '?':
        ans[i] = '1'
        if n < int(''.join(ans), 2):
            ans[i] = '0'

if int(''.join(ans), 2) <= n:
    print(int(''.join(ans), 2))
else:
    print(-1)