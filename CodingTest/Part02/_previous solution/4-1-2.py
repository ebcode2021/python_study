# 공간의 크기
n = int(input())

# 지도
travel_map = list(map(str, input().split()))

############# 간접 접근 했으므로 값이 변경되지 않음
for map in travel_map :
  print("map의 값은 -> ", map)
  if map == 'L' :
    map = [-1, 0]
  elif map == 'R' :
    map = [1, 0]
  elif map == 'U' :
    map = [0, -1]
  else :
    map = [0, 1]

print("변환 후 -> ", travel_map)

for i in range(len(travel_map)) :
  if travel_map[i] == 'L' :
    travel_map[i] = [0, -1]
  elif travel_map[i] == "R" :
    travel_map[i] = [0, 1]
  elif travel_map[i] == 'U' :
    travel_map[i] = [-1, 0]
  else :
    travel_map[i] = [1, 0]

# 여행자 위치
travel_location = [1,1]

for travel in travel_map :
  # 범위를 벗어난 경우에는 지도를 무시하는 조건
  if travel_location[0] + travel[0] < 1 or travel_location[0] + travel[0] > n or travel_location[1] + travel[1] < 1 or travel_location[1] + travel[1] > n :
    pass
  else :
     travel_location[0] += travel[0]
     travel_location[1] += travel[1]
  
print(travel_location[0], travel_location[1])

