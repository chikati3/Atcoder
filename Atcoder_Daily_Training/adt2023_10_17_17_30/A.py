K = int(input())

H = str(21 + K//60)
M = str(0 + K % 60)
print(H + ':' + M.zfill(2))