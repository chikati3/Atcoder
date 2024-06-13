S = input()

zero = S.count('00')
s = S.replace('00', '')
print(len(s) + zero)