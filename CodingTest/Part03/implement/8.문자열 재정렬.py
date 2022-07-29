strings = input()
sum = 0
new_str = []

for string in strings :
    if string >= '0' and string <= '9' :
        sum += int(string)
    else :
        new_str += string
new_str.sort()

if sum :
    new_str.append(str(sum))

print(''.join(new_str))