s = input()
t = input()

left = [True] * (len(t) + 1)
right = [True] * (len(t) + 1)
for i in range(len(t)):
    if s[i] == '?' or t[i] == '?' or s[i] == t[i]:
        left[i+1] = left[i]
    else:
        left[i+1] = False
    
    if s[-(i+1)] == '?' or t[-(i+1)] == '?' or s[-(i+1)] == t[-(i+1)]:
        right[i+1] = right[i]
    else:
        right[i+1] = False

n = len(t)
for i in range(n+1):
    if left[i] and right[n-i]:
        print('Yes')
    else:
        print('No')