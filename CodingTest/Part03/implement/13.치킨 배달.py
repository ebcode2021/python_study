# 도시 크기 n x n, 남길 치킨집 m
city_size, future_kfc_cnt = map(int, input().split())
current_kfc_cnt = 0
city_data = []
kfc_location = []
chicken_distance = []

# city_data 저장 및 kfc_location, current_kfc_cnt 저장
def basic_inform(city_size) :
	global current_kfc_cnt

	for x in range (city_size) :
		# city 정보 저장
		# 깊은 복사가 이루어지고 있어서. list는 mutable한 객체.......
		tmp_data = list(map(int, input().split()))
		city_data.append(tmp_data)
		# kfc location 저장
		while (2 in tmp_data) :
			y = tmp_data.index(2)
			current_kfc_cnt += 1
			kfc_location.append([x,y])
			tmp_data.remove(2)

basic_inform(city_size)

print(city_data)