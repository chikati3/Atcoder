N = int(input())
S = list(input())
Q = int(input())

flip = 0
for _ in range(Q):
    T, A, B = map(int, input().split())
    A -= 1
    B -= 1
    if T == 1:
        if flip == 1:
            A = (A + N) % (2 * N)
            B = (B + N) % (2 * N)
        S[A], S[B] = S[B], S[A] 
    elif T == 2:
        flip = 1 - flip
if flip == 1:
    print(''.join(S[N:] + S[:N]))
else:
    print(''.join(S))