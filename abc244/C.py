n = int(input())
used = [False] * (2*n+2)
used[0] = True
while True:
    if all(used):
        exit()
    for j in range(1, 2*n+2):
        if used[j] == False:
            used[j] = True
            print(j)
            break
    x = int(input())
    used[x] = True