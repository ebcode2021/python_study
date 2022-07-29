data = input()
x = ord(data[0]) - 96
y = int(data[1])

move_x = [2, 2, -2, -2, 1, -1, 1, -1]
move_y = [1, -1, 1, -1, 2, 2, -2, -2]
cnt = 0

for i in range(8) : 
    x += move_x[i]
    y += move_y[i]
    if not(x < 1 or x  > 8 or y < 1 or y > 8) :
        cnt += 1
    x -= move_x[i]
    y -= move_y[i]

print(cnt)