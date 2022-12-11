# n : 볼링공의 개수, m : 볼링공의 무게
n, m = map(int, input().split())
list_ball = list(map(int, input().split()))
cnt = 0

for i in range(n - 1) :
	for j in range (i + 1, n) :
		if list_ball[i] != list_ball[j] :
			cnt += 1
	i += 1

print(cnt)