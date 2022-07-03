###### 문제풀이1 : 자유

# 가게의 부품 개수
n = int(input())
list_n = list(map(int, input().split()))

# 손님의 부품 수
m = int(input())
list_m = list(map(int, input().split()))

for i in range(m) :
  result = n
  while(result>=1) :
    result -= 1
    if(list_m[i] == list_n[result-1]) :
      print("yes", end=' ')
      break
    if(result == 1) :
      print("no", end=' ')



###### 문제풀이2 : 이진 탐색 소스코드
def binary_search(array, target, start, end) :
  while start <= end :
    mid = (start + end) // 2
    if array[mid] == target :
      return mid
    elif array[mid] > target :
      end = mid - 1
    else :
      start = mid + 1
  return None

n = int(input())

array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x :
  result = binary_search(array, i, 0, n-1)
  if result != None :
    print('yes', end= ' ')
  else :
    print('no', end =' ')


###### 문제풀이3 : 이진 탐색 소스코드
n = int(input())
array = [0] * 1000001

for i in input().split() :
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x :
  if array[i] == 1 :
    print('yes', end=' ')
  else :
    print('no', end=' ')


###### 문제풀이4 : 집합 자료형
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x :
  if i in array :
    print('yes', end=' ')
  else :
    print('no', end=' ')