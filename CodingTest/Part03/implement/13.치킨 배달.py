from itertools import product, permutations, combinations

def chicken_distance(return_chicken, map) :
	for _ in range(return_chicken) :
		
	return (distance)

size, chicken_shop_cnt = map(int, input().split())
my_map = []
chicken_location = []

for i in range(size) :
	my_map.append(list(map(int, input().split())))
	while my_map[i].index(2) != -1 :
		chicken_location.append([i, my_map[i].index(2)])

return_chickens = list(permutations(chicken_location, chicken_shop_cnt))
min_location = 99999

for return_chicken in len(return_chickens) :
	if min_location > chicken_distance(return_chicken, my_map) :
		min_location = chicken_distance(return_chicken, my_map)
 
print(min_location)