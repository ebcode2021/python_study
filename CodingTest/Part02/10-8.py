# 도시 분할 계획

# 집 : n개, 길 : m개
n, m = map(int, input().split())
parent = [0] * (n+1)

# 간선을 담을 리스트아 최종 비용을 담을 변수
load = []
result = 0

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x) :
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

for i in range(1, n+1) :
  parent[i] = i

for _ in range(m) :
  a, b, c = map(int, input().split())
  load.append((c, a, b))

# 간선을 비용순으로 정렬
load.sort()
print("load sort 결과*********")
print(load)
last = 0

# 간선을 하나씩 확인
for edge in load :
  c, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    result += c
    last = c
  
print(result - last)

