# 답안 예시
h = int(input())
count = 0

for i in range(h+1) :
  for j in range(60) :
    for k in range(60) :
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k) :
        count+= 1

print(count)



# 잘못 된 풀이 (경우의 수가 복잡하다)

n = int(input())
count = 0
# 00시 00분 00초
# 시 -> 3시이전이면 0. 12시 이전이면 3시때. 12시 이후면 13시때. 23이면 23시.
# (1시간에) 분 -> 1

#1시간이면 60분. 3600초

# 시에 3이 있는 경우
if n>=3 and n <= 11 :
  count += 3600*1 
  count -= (60 * 5 + 60 * 10)
  count -= (5 + 10)
elif n>=12 and n<=22 :
  count += 3600*2
  count -= (60 * 5 + 60 * 10) * 2
  count -= (5 + 10) * 2

elif n>=23 :
  count += 3600*3
  count += (60 * 5 + 60 * 10) * 3
  count += (5 + 10) * 3
else :
  pass

# 1시간 동안 분에 3이 있을 경우
count += (60 * 5 + 60 * 10) * n

# 1시간 동안 초에 3이 있을 경우
count += (5 + 10) * n 

print(count)


