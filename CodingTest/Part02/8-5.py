# 정수
x = int(input())

# 연산하는 최소 횟수
min_cnt = [0] * 30001

# 보텀업 진행
for i in range(2, x+1) :
  # 현재의 수에서 1을 빼는 경우
  min_cnt[i] = min_cnt[i-1] + 1
  if i % 2 == 0 :
    min_cnt[i] = min(min_cnt[i], min_cnt[i // 2]+1)
  if i % 3 == 0 :
    min_cnt[i] = min(min_cnt[i], min_cnt[i//3]+1)
  if i % 5 == 0 :
    min_cnt[i] = min(min_cnt[i], min_cnt[i//5] + 1)

print(min_cnt)