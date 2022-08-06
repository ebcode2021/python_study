n = int(input())
my_list = []

for _ in range(n) :
	my_list.append(int(input()))

my_list.sort()

for i in range(n) :
	print(my_list[i])