input_number = int(input())
i = 0

for i in range(1, input_number+1) :
  if i % 10 in [3, 6, 9] :
    print("X", end=" ")
  else : 
    print(i, end=" ")
  

  