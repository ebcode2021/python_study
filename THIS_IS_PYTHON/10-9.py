# 동빈이가 들을 강의 개수
from collections import deque
from copy import copy


n = int(input())

# 진입 차수
indegree = [0] * (n+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [ [] for i in range(n+1)]

# 각 강의 시간 0으로 초기화
time = [0] * (n+1)

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1, n+1) :
  data = list(map(int, input().split()))
  time[i] = data[0]
  for x in data[1:-1] :
    indegree[i] += 1
    graph[x].append(i)

# 위상 정렬 함수
def topology_sort() :
  result = copy.deepcopy(time) # deepcopy는 result 리스트 변수의 값을 복사
  q = deque()

  for i in range(1, n+1) :
    if indegree[i] == 0 :
      q.append(i) 

  # 큐가 빌 때까지 반복
  while q :
    # 큐에서 원소 꺼내기
    now = q.popleft()
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now] :
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0 :
        q.append(i)
  
  # 위상 정렬을 수행한 결과 출력
  for i in range(1, n+1) :
    print(result[i])
