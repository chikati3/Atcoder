from functools import lru_cache


n = int(input())

#メモ化再帰
@lru_cache(maxsize=None)
def f(x):
    if x == 0:
        return 1
    else:
        return f(x//2) + f(x//3)
print(f(n))