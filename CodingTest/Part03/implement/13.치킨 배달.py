# 도시 크기 n x n, 남길 치킨집 m
city_size, future_kfc_size = map(int, input().split())
city_data = []
current_kfc_size = 0

for _ in range (city_size) :
	tmp_data = list(map(int, input().split()))
	current_kfc_size += tmp_data.count(2)
	city_data.append(tmp_data)

print(city_data)
print(current_kfc_size)