from math import sqrt


a, b = map(int, input().split())

def f(x):
    return b * x + a / sqrt(x+1)

# 三分探索
left = 0
right = 10**18
while right - left > 2:
    midl = (left + left + right ) // 3
    midr = (left + right + right) // 3
    if f(midl) < f(midr):
        right = midr
    else:
        left = midl
print(min(f(left), f(left+1), f(left+2)))