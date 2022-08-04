min = int(input())
max = int(input())

decimal_lists = []

for i in range(min, max + 1) :
    decimal_lists.append(i)

num = 2

while num != max :
    if 1 in decimal_lists :
        decimal_lists.remove(1)
    if not decimal_lists :
        break
    for decimal_list in decimal_lists :
        if decimal_list % num == 0 and decimal_list > num :
            decimal_lists.remove(decimal_list)
    num += 1

if not decimal_lists :
    print(-1)
else :
    print(sum(decimal_lists))
    print(decimal_lists[0])
        