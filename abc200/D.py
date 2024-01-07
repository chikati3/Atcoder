N = int(input())
A = list(map(int, input().split()))

n = min(N, 8)
a_list = [[] for _ in range(200)]
for i in range(2**n):
    num = 0
    b_list = []
    for j in range(n):
        if i >> j & 1:
            num += A[j]
            b_list.append(j+1)
    x = num % 200
    if len(a_list[x]) :
        print('Yes')
        print(len(a_list[x]), *a_list[x])
        print(len(b_list), *b_list)
        exit()
    a_list[x] = b_list
print('No')