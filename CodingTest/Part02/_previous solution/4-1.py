n = input().split()
x,y = 1,1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 확인
for plan in plans :
  for i in range(len(move_types)) :
    if plan == move_types[i] :
      nx = x + dx[i]
      ny = y+ dy[i]
    # 공간을 벗어나는 경우
    if nx <1 or ny <1 or nx>n or ny>n :
      continue
    x,y = nx, ny


print(x,y)

# 다른 방식 풀이

n = int(input())
x,y = 1, 1
nx, ny = 1, 1
plans = list(map(str, input().split()))

for i in range(len(plans)) :
  print(plans[i])

  if plans[i] == "L" and ny >= 2 :
    ny = y -1
  elif plans[i] == 'R' and ny < n :
    ny = y + 1
  elif plans[i] == 'U' and nx >=2 : 
    nx = x - 1
  elif plans[i] == 'D'and nx < n : 
    nx = x + 1

  x,y = nx, ny



print(x,y)
