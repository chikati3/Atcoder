N = int(input())
A = list(map(int, input().split()))
X = int(input())

a = sum(A)
if X < a:
    num = 0
    for i in range(N):
        num += A[i]
        if X < num:
            print(i+1)
            exit()
else:
    cnt = X // a * N
    X %= a
    num = 0
    for i in range(N):
        num += A[i]
        if X < num:
            print(cnt + i+1)
            exit()