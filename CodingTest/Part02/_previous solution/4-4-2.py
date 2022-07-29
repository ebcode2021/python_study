# 맵의 크기
n, m = map(int, input().split())

# 게임 캐릭터의 좌표 + 방향(d)
row, col, d = map(int, input().split())

# map을 입력받기
char_map = []
for i in range(n) :
  char_map.append(list(map(int, input().split())))

# 네 방향을 리스트 (북, 동, 남, 서)
four_direction_x = [-1, 0, 1, 0]
four_direction_y = [0, 1, 0, -1]

# 캐릭터가 바라보고 있는 방향 리스트(북, 동, 남, 서)
character_direction = [0, 1, 2, 3]

# 캐릭터가 왼쪽 방향으로 일단 돌아야됨.
now_direction = character_direction[d-1]

# 방문한 횟수
visit_cnt = 1
maximum_spin = 1


def move_location (row, col, d) :
  global visit_cnt
  global maximum_spin 

  new_x = row + four_direction_x[now_direction]
  new_y = col + four_direction_y[now_direction]

  while(maximum_spin<5) :
    if(char_map[new_x][new_y] == 0) : # 방문한 적 없을 때
      row = new_x
      col = new_y
      char_map[row][col] = 2
      maximum_spin = 1
      visit_cnt += 1
    else : # 바다거나 이미 방문한 곳일 때
      new_x = row + four_direction_x[now_direction-maximum_spin]
      new_y = col + four_direction_y[now_direction-maximum_spin]
      maximum_spin+=1

move_location(row, col, d)

print(visit_cnt)