import numpy as np


n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

an = np.poly1d(a[::-1])
cn = np.poly1d(c[::-1])

ans = cn / an
ans = list(map(int, ans[0]))
print(*ans[::-1])