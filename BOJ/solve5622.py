strings = input()
sum = 0

for string in strings :
	if string <= 'R' :
		sum += (ord(string) - 59) // 3 + 1
	elif string == 'S' :
		sum += (ord(string) - 59) // 3
	elif string >= 'T' and string <= 'V' :
		sum += 9
	else :
		sum += 10
print(sum)