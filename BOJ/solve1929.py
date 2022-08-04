import math

def check_decimal(number) :
	if number == 1 :
		return
	start = 2
	while start <= math.sqrt(number) :
		if number % start == 0 :
			return
		start += 1
	print(number)

m, n = map(int, input().split())

for i in range(m, n + 1) :
	check_decimal(i)

# 에라토스테네스의 체 원리를 쓰면 더 느리지 않을까? 최적화..?
# pypy3 에서는 통과되지만, python3 에서는 통과 ㄴㄴ 흐음...