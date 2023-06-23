
n = int(input())

num = 3*10**5
prime = [True] * (num+1)
prime_num = []
for i in range(2, num+1):
    if prime[i] == True:
        prime_num.append(i)
        for j in range(i+i, num+1, i):
            prime[j] = False

p_len = len(prime_num)
ans = 0
for i in range(p_len):
    a = prime_num[i]
    if n < a*a:
        break
    for j in range(i+1, p_len):
        b = prime_num[j]
        if n < a*a*b:
            break
        else:
          left = j+1
          right = p_len
          while right - left > 1:
              mid = (right + left) // 2
              c= prime_num[mid]
              if a*a*b*c*c <= n:
                  left = mid
              else:
                  right = mid
          if i < j < left and left < right:
            c = prime_num[left]
            if a*a*b*c*c <= n:
              ans += left - j
            else:
                break
print(ans)