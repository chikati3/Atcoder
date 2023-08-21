n, a, b = map(int, input().split())

def f(n):
    return n * (n+1) // 2

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
def lcm(x, y):
    return x * y // gcd(x, y)

ans = f(n) - f(n//a)*a - f(n//b)*b
lm = lcm(a, b)
ans += f(n//lm) * (lm)
print(ans)