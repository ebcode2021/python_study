# union과 find 연산을 사용한다.

# 같은 팀 여보 확인 연산에 대한 연산 결과를 출력

# n은 존재하는 학생의 수, m은 연산의 개수
n, m = map(int, input().split())

# 입력 받을 값 리스트에 저장
calc_list = []

for _ in range(m) :
  calc_list.append(list(map(int, input().split())))

# 같은 팀 확인 위해 부모 리스트 생성
parent = [0] * (n+1)
for i in range(1, n+1) :
  parent[i] = i

def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

def find_parent(parent, x) :
  if parent[x] != x :
    return find_parent(parent, parent[x])
  return x


for list in calc_list :
  if list[0] == 1 : # 같은 팀 여부 확인(find)
    boolean = find_parent(parent, list[1]) == find_parent(parent, list[2])   
    if(boolean) :
      print("YES")
    else :
      print("NO") 
    pass
  else : # 팀 합치기(union)
    union_parent(parent, list[1], list[2])


