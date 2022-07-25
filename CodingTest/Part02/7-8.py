# 떡의 길이와 손님이 요청한 길이
n, m = map(int, input().split())

list_dduck = list(map(int, input().split()))

start = 0
end = max(list_dduck)

# 이진 탐색 수행 (반복)
result = 0

while (start <= end) :
  total = 0
  mid = (start + end) // 2
  for x in list_dduck :
    if x > mid :
      total += x - mid
  if total < m :
    end = mid - 1
  else :
    result = mid
    start = mid + 1

print(result)