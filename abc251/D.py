w = int(input())

ans = []
ans.append(1000000)
for i in range(1, 100):
    ans.append(i)
    ans.append(i*100)
    ans.append(i*10000)
print(len(ans))
print(*ans)