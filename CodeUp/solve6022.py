d = input()

sep = 2
lastIndex = len(d) - sep

for i in range(0, len(d), sep) :
  if i < (lastIndex):
    print(d[i:i+2], end=' ')
  else:
    print(d[i:i+2], end='')
    
# 두 번째 풀이 방법
date = input()

for i in range(0, 6, 2) :
  print(date[i:i+2], end=" ")