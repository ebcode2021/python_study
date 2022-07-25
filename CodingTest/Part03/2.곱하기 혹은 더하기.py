num = str(input())
calc_list = []

for i in range(len(num)) :
    calc_list.append(int(num[i]))

i = 0
result = calc_list[0]
while i < len(num) - 1 :
    if calc_list[i] == 0 or calc_list[i + 1] == 0:
        result += calc_list[i + 1]
    else :
        result *= calc_list[i + 1]
    i += 1

print(result)