# 식량 창고의 개수
from xxlimited import foo


n = int(input())

# 식량창고에 저장된 식량의 개수
food_storage = list(map(int, input().split()))

# dp 초기화
d = [0] * 100

d[0] = food_storage[0]
d[1] = max(d[0], food_storage[1])

for i in range(2, n) :
  d[i] = max(d[i-1], d[i-2] + food_storage[i])

print(d[n-1])