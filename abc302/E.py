#pypy3使用

n, q = map(int, input().split())

s = [set() for _ in range(n)]
ans = n
for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        _, u, v = que
        u -= 1
        v -= 1
        if len(s[u]) == 0:
            ans -= 1
        if len(s[v]) == 0:
            ans -= 1
        s[u].add(v)
        s[v].add(u)
    else:
        _, v = que
        v -= 1
        if len(s[v]) != 0:
          for ui in s[v]:
              s[ui].discard(v)
              if len(s[ui]) == 0:
                  ans += 1
          s[v].clear()
          ans += 1
    print(ans)
