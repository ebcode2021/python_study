data = input()
data_len = len(data)
sum = 0

for i in range(data_len // 2) :
    sum += int(data[i])

for i in range(data_len // 2, data_len) :
    sum -= int(data[i])

if not sum :
    print("LUCKY")
else :
    print("READY") 