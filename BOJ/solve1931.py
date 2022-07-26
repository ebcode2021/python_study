room_num = int(input())
room_data = []

for _ in range(room_num) :
    room_data.append(list(map(int, input().split())))

room_data.sort(key = lambda x : (x[1], x[0]))

start = 0
cnt = 0

for a, b in room_data:
    if a >= start:
        cnt += 1
        start = b

print(cnt)