
n = int(input())
s = input()

cnt = 0
ans = []
for si in s:
    if si == '(':
        cnt += 1
        ans.append(si)
    elif si == ')':
        if 1 <= cnt:
            while ans[-1] != '(':
                ans.pop()
            ans.pop()
            cnt -= 1
        else:
            ans.append(si)
    else:
        ans.append(si)
print(''.join(ans))