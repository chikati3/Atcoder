N, M = map(int, input().split())
a = [input() for _ in range(N*2)]

score = [[0, i] for i in range(N*2)]

janken = ['GC', 'CP', 'PG']
x = 0
while x < M:
    for i in range(0, N*2, 2):
        l, r = score[i][1], score[i+1][1]
        if a[l][x] + a[r][x] in janken:
            for j in range(N*2):
                if score[j][1] == l:
                    score[j][0] += 1
        if a[r][x] + a[l][x] in janken:
            for j in range(N*2):
                if score[j][1] == r:
                    score[j][0] += 1

    score = sorted(score, key=lambda x: x[1])
    score = sorted(score, key=lambda x: x[0], reverse=True)
    x += 1

for _, s in score:
    print(s + 1)