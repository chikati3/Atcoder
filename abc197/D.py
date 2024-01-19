import cmath
import math


N = int(input())
x0, y0 = map(int, input().split())
x2, y2 = map(int, input().split())

p0 = complex(x0, y0)
p2 = complex(x2, y2)

#中点
o = (p0 + p2) / 2
r = cmath.rect(1, 2 * math.pi / N)
ans = (p0 - o) * r + o
print("%.10f %.10f" % (ans.real, ans.imag))