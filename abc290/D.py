from math import gcd


t = int(input())

for _ in range(t):
    n, d, k = map(int, input().split())
    k -= 1
    g = gcd(n, d)
    # 周期
    x = n // g
    # 印の回数
    y = k // x
    # 進んだ合計マス
    print((d * k + y) % n)