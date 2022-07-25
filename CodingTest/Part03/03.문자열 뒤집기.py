datas = list(str(input()))
zero_check = 0
one_check = 0
break_point = 0

if datas[0] == '0' :
	zero_check += 1
else :
	one_check += 1

for i in range(len(datas) - 1) :
	if datas[i] != datas[i + 1] :
		break_point += 1
		if datas[i + 1] == '0' :
			zero_check += 1
		else :
			one_check += 1

if break_point == 0 :
	print(0)
elif break_point == 1 or break_point == 2 :
	print(1)
else :
	print(zero_check if zero_check <= one_check else one_check)