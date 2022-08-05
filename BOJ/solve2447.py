# 3의 거듭제곱으로 주어짐
n = int(input())
col = [['*' for col in range(n)] for row in range(n)]

def isDec(n) :
	idx = -1
	while n > 1 :
		n /= 3
		idx += 1
	return (idx)

def fibonacci(n) :
	m = isDec(n)
	if n == 1 :
		return
	for i in range(3 ** m) :
		for j in range(3 ** m) :
			col[3 ** m + j][3 ** m + i] = ' '
	n /= 3
	fibonacci(n)

fibonacci(n)

for i in range(n) :
		print(''.join(col[i]))