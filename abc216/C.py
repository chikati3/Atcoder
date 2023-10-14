N = int(input())

ans = ''
for i in range(120):
    if N % 2 == 0:
        N //= 2
        ans += 'B'
    else:
        N -= 1
        ans += 'A'
    
    if N == 0:
        break
print(ans[::-1])