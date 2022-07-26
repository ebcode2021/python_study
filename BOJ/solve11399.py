man = int(input())

time_list = list(map(int, input().split()))
time_list.sort()
new_list = []
new_list.append(time_list[0])

for i in range(1, man) :
    new_list.append(sum(time_list[0 : i + 1]))

print(sum(new_list))

# 모범답안
num = 0
for i in range(man) :
    for j in range(i + 1) :
        num += time_list[j]

print(num)