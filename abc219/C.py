X = input()
N = int(input())

d = {}
for i in range(26):
    d[X[i]] = str(i+10)

S = []
nums = []
for i in range(N):
    s = input()
    num = ''
    for si in s:
        num += d[si]
    S.append(s)
    nums.append([num, i])
nums.sort()

for _, i in nums:
    print(S[i])