number_cnt = int(input())
input_number = list(map(int, input()))
cnt = 0

while number_cnt :
  cnt += input_number[number_cnt - 1]
  number_cnt -= 1

print(cnt)