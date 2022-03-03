# 내가 푼 방법(for문 사용)
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first_number = data[n-1]
second_number = data[n-2]

sum = 0
count = 1

for i in range(m) :
  if(count>k) :
    sum += second_number
    count = 1
    continue

  sum += first_number
  count += 1

print(sum)


# 책 해설1 (while문 사용)
n,m,k = map(int, input().split())
data = list(int, input().split())

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True :
  for i in range(k) :
    if m == 0 :
      break
    result += first
    m -= 1
  if m == 0 :
    break
  result += second
  m -= 1

print(result)


# 책 해설2 (수열 규칙 사용)
n, m, k = map(int, input().split())
data = list(int, input().split())

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)