# 미로 상자 구조 입력
table = []

for i in range(10) :
 table.append(list(map(int,input().split())))

# 오른쪽 이동 / 아래쪽 이동
move_right = [0, 1]
move_down = [1, 0]

# 시작점 확인
table[1][1] = 9

i, j = 1, 1

while True :
  
  # 오른쪽으로 지나갈 수 있을 때
  if table[i][j+1] != 1 :
    if(table[i][j+1]==2) :
      table[i][j+1] = 9
      break
    table[i][j+1] = 9
    j += 1
    continue
  # 아래쪽으로 지나갈 수 있을 때
  elif table[i+1][j] != 1 :
    if(table[i+1][j]==2) :
      table[i+1][j] = 9
      break
    table[i+1][j] = 9
    i += 1
    continue
  # 이동 불가일 때
  else : 
    break


for rows in table :
  for items in rows :
    print(items, end=' ')
  print()



