
from functools import lru_cache


n = int(input())
mod = 998244353
inv = pow(5, mod-2, mod)

# メモ化再帰
# サイコロも目は2~6で考える(1/5)
# nからスタートして1になる確率
# 約数を求める
@lru_cache(maxsize=None)
def main(x):
    if x <= 1: return x

    ans = 0
    for i in range(2, 6+1):
        if x % i == 0:
            ans += main(x // i)
    ans = ans * inv % mod
    return ans
print(main(n))