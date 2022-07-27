strings = input()
croa_lists = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croa_cnt = 0
normal_cnt = 0
first_len = len(strings)

i = 0
while   i <= (first_len - 1) :
    if strings[i : i + 3] == "dz=" :
        croa_cnt += 1
        i += 3
    elif strings[i : i + 2] in croa_lists :
        croa_cnt += 1
        i += 2
    else :
        normal_cnt += 1
        i += 1

print(croa_cnt + normal_cnt)

# 모범답안 (아니 이리 간단..)

for i in croa_lists :
    strings = strings.replace(i, 'a')
print(len(strings))