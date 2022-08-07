mines = list(map(int, input().split()))

model = [1, 1, 2, 2, 2, 8]
idx = 0

for mine in mines :
	if mine == model[idx] :
		model[idx] = 0
	else :
		model[idx] -= mine
	idx += 1

values = " ".join(map(str, model))
print(values)