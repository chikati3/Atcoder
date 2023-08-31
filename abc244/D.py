s = input()
t = input()

#転倒数
#偶置換、奇置換
x = ['R G B', 'G B R', 'B R G']
if (s in x) == (t in x):
    print('Yes')
else:
    print('No')