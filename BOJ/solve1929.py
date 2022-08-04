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