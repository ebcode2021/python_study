# 첫 번째 역순 정렬

n = int(input())

list1 = []

for _ in range(n) :
  list1.append(int(input()))

list1.sort(reverse=True)

print(list1)

for i in list1 :
  print(i, end=' ')

# 두 번째 역순 정렬
n = int(input())

list2 = []

for _ in range(n) :
  list2.append(int(input()))

array = sorted(list2, reverse=True)
print(array)

for i in array : 
  print(i, end=' ')