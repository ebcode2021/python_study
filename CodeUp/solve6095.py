n = int(input())

n_list = []

for i in range(20) :
  n_list.append([])
  for j in range(20) :
    n_list[i].append(0)


for i in range(n) :
  x, y = map(int, input().split())
  n_list[x][y] = 1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(n_list[i][j], end=' ')
  print()