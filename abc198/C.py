R, X, Y = map(int, input().split())

def f(x, y):
    return (x*x + y*y) ** 0.5

z = f(X, Y)

if z % R == 0:
    print(int(z // R))
elif z == R:
    print(1)
elif z < R:
    print(2)
else:
    print(int(-(-z // R)))