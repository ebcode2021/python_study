# 가로 길이
n = int(input())

# dp 초기화
d = [0] * 1001

# n이 홀수 일 때, n이 짝수일 때

d[1] = 1
d[2] = 3

for i in range(2, n) :
  if n % 2 == 0 : # 짝수
    d[i+1] = 1 + d[i-1] * 3
  else : # 홀수
    d[i+1] = d[i-1] * 3 + (d[i]-1)


print(d[n]%796796)


