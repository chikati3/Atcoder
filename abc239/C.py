x1, y1, x2, y2 = map(int, input().split())

def f(x, y, x1, y1):
    return (x-x1)**2 + (y-y1)**2

ans = 'No'
for i in range(-2, 3):
    for j in range(-2, 3):
        if f(x1+i, y1+j, x1, y1) == f(x1+i, y1+j, x2, y2) == 5:
            ans = 'Yes'
print(ans)