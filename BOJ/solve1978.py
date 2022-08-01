num = int(input())
num_lists = list(map(int, input().split()))
res = 0

for num_list in num_lists :
    cnt = 2
    flag = 1
    if num_list == 1 :
            continue
    while cnt < num_list:
        if num_list % cnt == 0 :
            flag = 0
            break
        cnt += 1
    if flag :
        res += 1

print(res)


