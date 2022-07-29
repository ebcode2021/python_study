import re

expression = input()
ex_list = re.split('[+-]+', expression)
operation_list = re.findall('[^0-9]', expression)
min_sum = int(ex_list[0])

for i in range(len(operation_list) - 1) :
    if operation_list[i] == '-' and operation_list[i+1] == '+' :
        operation_list[i+1] = '-'

for i in range(1, len(ex_list)) :
    tmp = int(ex_list[i])
    if (operation_list[i-1] == '-') :
        tmp *= -1
    min_sum += tmp

print(min_sum)
