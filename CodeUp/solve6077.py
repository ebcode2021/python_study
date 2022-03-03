num = int(input())
evenSum = 0

for i in range(0, num+1) :
  if(i%2 == 0) :
    evenSum += i

print(evenSum)