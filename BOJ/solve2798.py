from itertools import combinations

n, large = map(int, input().split())
n_list = list(map(int, input().split()))

three_list = list(combinations(n_list, 3))
my_list = []

for my_comb in three_list :
	if sum(my_comb) > large :
		continue
	else :
		my_list.append(sum(my_comb))
print(max(my_list))