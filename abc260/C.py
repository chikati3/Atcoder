from functools import lru_cache


n, x, y = map(int, input().split())

@lru_cache(None)
def red(n):
    if n <= 1:
        return 0
    else:
        return red(n-1) + blue(n) * x

@lru_cache(None)
def blue(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return red(n-1) + blue(n-1) * y

print(red(n))