# 도시 크기 n x n, 남길 치킨집 m
city_size, future_kfc_cnt = map(int, input().split())
current_kfc_cnt = 0
city_data = []
move_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

kfc_locations = []
chicken_distances = []

def basic_inform(city_size) :
	global current_kfc_cnt

	for x in range (city_size) :
		tmp_data = list(map(int, input().split()))
		current_kfc_cnt += tmp_data.count(2)
		city_data.append(tmp_data)
		# kfc location 저장
		while (2 in tmp_data) :
			y = tmp_data.index(2)
			kfc_locations.append([x,y])
			tmp_data.remove(2)

def calc_chicken_distance(x, y, chicken_distance) :
	for move_direction in move_directions :
		if not ( 0 <= x + move_direction[0], y + move_direction[1] <= city_size) :
			continue
		if is_home(x + move_direction[0], y + move_direction[1]) :
			return (chicken_distance)
		else :
			print(move_direction[0])
			calc_chicken_distance(x + move_direction[0], y + move_direction[1], chicken_distances + 1)

def is_home(move_x, move_y) :
	if city_data[move_x][move_y] == 1 :
		return (1)
	return (0)

basic_inform(city_size)
for kfc_location in kfc_locations :
	x, y = kfc_location[0], kfc_location[1]
	chicken_distances.append(calc_chicken_distance(x, y, 1))

sorted(chicken_distances)
print(sum(chicken_distances[0 : future_kfc_cnt]))