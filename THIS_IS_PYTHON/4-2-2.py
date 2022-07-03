# 끝나는 시각
n = int(input())

# 시작 시간 / 종료 시간
start_hour, start_min, start_sec = 0, 0, 0
end_hour, end_min, end_sec = n, 59, 59

start_time = start_hour * 3600 + start_min * 60 + start_sec
end_time = end_hour * 3600 + end_min * 60 + end_sec
three_cnt = 0

while(start_time < end_time) :
  start_sec += 1

  if(start_sec == 60) :
    start_min += 1
    start_sec = 0
  
  if(start_min == 60) :
    start_hour += 1
    start_min = 0
  
  if("3" in str(start_hour)+ str(start_min) + str(start_sec)) :
    three_cnt += 1

  start_time += 1

print(three_cnt)
  
