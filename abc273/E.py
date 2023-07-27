q = int(input())
qs = [input().split() for i in range(q)]

#親
par = [-1]
#末尾
val = [-1]
ans = []
#親の場所
now = 0
note = {}
for cs, *rem in qs:
    if cs == "ADD":
        x = rem[0]
        par.append(now)
        val.append(x)
        now = len(par) - 1
    if cs == "DELETE":
        if now:
            now = par[now]
    if cs == "SAVE":
        y = rem[0]
        note[y] = now
    if cs == "LOAD":
        z = rem[0]
        now = note.get(z, 0)
    ans.append(val[now])

print(*ans)