horse_location = input()

# 체스 말의 행과 열의 위치
horse_row = int(horse_location[1:])
horse_col = ord(horse_location[0:1]) - 96

possible_cnt = 0

def move_cnt(a, b) :
  global possible_cnt
  if(a - 2 > 0) :
    if(b - 1 > 0) :
      possible_cnt += 1
    if(b + 1 < 9) :
      possible_cnt += 1
  
  if(a + 2 < 9) :
    if(b - 1 > 0) :
      possible_cnt += 1
    if(b + 1 < 9) :
      possible_cnt += 1


move_cnt(horse_row, horse_col)
move_cnt(horse_col, horse_row)

print(possible_cnt)


