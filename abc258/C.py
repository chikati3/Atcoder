n, q = map(int, input().split())
s = input()

idx = 0
for _ in range(q):
    t, x = map(int, input().split())

    if t == 1:
        idx = (idx - x) % n
    else:
        x -= 1
        print(s[(idx+x)%n])