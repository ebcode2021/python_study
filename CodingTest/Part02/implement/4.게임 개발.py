# map size
n, m = map(int, input().split())

# gamer location
x, y, dir = map(int, input().split())

# detail_map
my_map = []
for i in range(n) :
    data = list(map(int, input().split()))
    my_map.append(data)

# 북, 동, 남, 서
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
max_value = 4
cnt = 1

dir -= 1
while max_value != 0 :
    for i in range(4) :
        if dir + i >= 4 :
            dir -= 4
        if dir + i < 0 :
            dir += 4
        new_x = x + direction[dir][0]
        new_y = y + direction[dir][1]
        if my_map[new_x][new_y] != 1:
            my_map[new_x][new_y] = 1
            x, y = new_x, new_y
            cnt += 1
            dir -= 1
            max_value = 4
            break
        else :
            dir -= 1
            max_value -= 1

print(cnt)