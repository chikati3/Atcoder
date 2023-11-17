S = input()

ok = []
ng = []
x = []
for i in range(10):
    if S[i] == 'o':
        ok.append(i)
    elif S[i] == 'x':
        ng.append(i)
    else:
        x.append(i)

ans = 0
for i in range(10000):
    i = str(i)
    i = i.zfill(4)
    ok_cnt, ng_cnt = 0, 0
    for o in ok:
        if str(o) in i:
            ok_cnt += 1
    for n in ng:
        if str(n) in i:
            ng_cnt += 1
    if len(ok) == ok_cnt and ng_cnt == 0:
        ans += 1
print(ans)