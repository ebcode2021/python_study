# 시뮬레이션 문제
room = int(input())
plans = list(map(str, input().split()))

# L, R, U, D
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

x = 1
y = 1

for plan in plans :
    tmp = move.index(plan)
    x += move_x[tmp]
    y += move_y[tmp]
    if not(x >= 1 and x <= room) or not(y >= 1 and y <= room) :
        x -= move_x[tmp]
        y -= move_y[tmp]
print(x, y)