s = input()
q = int(input())

def f(t, k):
    if t == 0:
        return ABC.index(s[k])
    elif k == 0:
        return ABC.index(s[0]) + t
    elif k % 2 == 0:
        return f(t-1, k//2) + 1
    else:
        return f(t-1, k//2) + 2

ABC = 'ABC'
for _ in range(q):
    t, k = map(int, input().split())
    k -= 1
    print(ABC[f(t, k) % 3])