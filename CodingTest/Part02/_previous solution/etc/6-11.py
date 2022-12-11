n = int(input())

stu_list = []
for _ in range(n) :
  stu_list.append(list(input().split()))

def setKey (stu_list) :
  return stu_list[1]

result = sorted(stu_list, key=setKey)

for stu in result :
  print(stu[0], end=' ')