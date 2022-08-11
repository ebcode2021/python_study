total_cnt = int(input())
cnt = int(input())
calc_cnt = 0

for _ in range(cnt) :
	good, count = map(int, input().split())
	calc_cnt += good * count

if calc_cnt == total_cnt :
	print("Yes")
else :
	print("No")