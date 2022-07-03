# 배열 원소의 개수, 바꿔치기 수
n, k = map(int, input().split())

list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

# 정렬
list_A.sort()
list_B.sort(reverse=True)

for i in range(k) :
  if list_A[i] < list_B[i] : 
    list_A[i], list_B[i] = list_B[i], list_A[i]

print(sum(list_A))




