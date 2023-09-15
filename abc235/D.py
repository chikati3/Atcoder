from collections import deque


a, N = map(int, input().split())

cnt = [-1] * (10**6+1)
cnt[1] = 0
d = deque()
d.append(1)
while d:
    x = d.popleft()
    xi = int(str(x%10) + str(x//10))
    if x * a <= 10**6 and cnt[x*a] == -1:
        cnt[x*a] = cnt[x] + 1
        d.append(x*a)
    if 10 <= x and x % 10 != 0 and xi <= 10**6 and cnt[xi] == -1:
        cnt[xi] = cnt[x] + 1
        d.append(xi)
print(cnt[N])