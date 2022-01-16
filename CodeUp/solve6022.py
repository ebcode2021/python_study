d = input()

sep = 2
lastIndex = len(d) - sep

for i in range(0, len(d), sep) :
  if i < (lastIndex):
    print(d[i:i+2], end=' ')
  else:
    print(d[i:i+2], end='')
    