# 얼음 틀의 크기
n, m = map(int, input().split())

ice_frame = []

# 얼음 틀 모양 입력
for i in range(n) :
  ice_frame.append(list(map(int, input())))

# 아이스크림 개수 확인
def ice_cream(x,y) :
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m :
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if ice_frame == 0 :
    # 해당 노드 방문 처리
    ice_frame[x][y] = 1
    # 상, 하, 좌,. 우 모두 재귀적으로 호출
    ice_cream(x-1, y)
    ice_cream(x, y-1)
    ice_cream(x+1, y)
    ice_cream(x, y+1)
    return True
  return False

ice_cream_cnt = 0
for i in range(n) :
  for j in range(m) :
    # 현재 위치에서 dfs 수행
    if ice_cream(i, j) == True :
      ice_cream_cnt += 1

print(ice_cream_cnt)