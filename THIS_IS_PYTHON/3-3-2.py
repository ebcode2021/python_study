n, m = map(int, input().split())
board = [[0]*n for i in range(m)]
arr_min = []

for row in range(n) :
  min = 10001
  board[row] = list(map(int, input().split()))

  for col in range(m) :
    if(board[row][col] < min) :
      min = board[row][col]
  
  arr_min.append(min)

arr_min.sort()
print(arr_min[n-1])
