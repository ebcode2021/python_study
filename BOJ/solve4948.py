max = 123456 * 2
a = [False, False] + [True] * (max - 1)
primes = []

for i in range(2, max + 1) :
	if a[i] :
		primes.append(i)
		for j in range(2 * i, max + 1, i) :
			a[j] = False

while 1 :
	n = int(input())
	if n == 0 :
		break
	cnt = 0

	for i in primes :
		if n < i <= 2 * n :
			cnt += 1
	print(cnt)