# 화폐의 종류 : n, 가치의 합 : m
n, m = map(int, input().split())

# 화폐 단위 입력 
array = list(map(int,input().split()))

# dp 초기화
d = [10001] * (m+1)

d[0] = 0
for i in range(n) :
  for j in range(array[i], m + 1) :
    if d[j - array[i]] != 10001 :
      d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001 : 
  print(-1)
else :
  print(d[m])
  