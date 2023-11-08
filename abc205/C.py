A, B, C = map(int, input().split())

if C % 2 == 0:
    A = A*A
    B = B*B

if A == B:
    print('=')
elif A < B:
    print('<')
else:
    print('>')