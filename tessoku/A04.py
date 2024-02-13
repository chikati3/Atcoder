N = int(input())

ans = ''
while N != 0:
    ans += str(N%2)
    N //= 2
while len(ans) < 10:
    ans += '0'

print(ans[::-1])