# 격자판의 세로(h), 가로(w)
h, w = map(int, input().split())

table = [[0] * w for _ in range(h)]


# 놓을 수 있는 막대의 개수(n)
n = int(input())

# 각 막대의 길이, 방향(가로 0, 세로 1), 좌표
for _ in range(n) :
  l, d, x, y = map(int, input().split())

  for column in range(l) :
    # 가로 방향
    if d == 0 :
      table[x-1][y+column-1] = 1
    # 세로 방향
    else :
      table[x+column-1][y-1] = 1
  

# 출력
for row in table:
  for item in row:
    print(item, end=' ')
  print()
