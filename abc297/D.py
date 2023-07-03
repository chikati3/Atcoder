
a, b = map(int, input().split())

ans = 0
while a != b:
    if a < b:
        a, b = b, a
    x = (a - 1) // b
    a -= x * b
    ans += x
print(ans)