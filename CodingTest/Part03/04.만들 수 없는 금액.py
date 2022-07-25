coin_cnt = int(input())
coin_data = list(map(int, input().split())).sort()

target = 1
for x in coin_data :
    if target < x :
        break
    target += x

print(target)
