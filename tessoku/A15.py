N = int(input())
A = list(map(int, input().split()))

A.append(0)
a = sorted(set(A))
num = {}
B = []
for i in range(N):
    if A[i] in num:
        B.append(num[A[i]])
        continue

    left = 0
    right = len(a) - 1
    while right - left > 1:
        mid = (right + left) // 2
        if A[i] <= a[mid]:
            right = mid
        else:
            left = mid
    B.append(right)
    num[A[i]] = right
print(*B)