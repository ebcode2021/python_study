# n : 외벽의 길이 | weak : 취약 지점의 위치가 담긴 배열 | dist : 각 친구가 1시간 동안 이동할 수 있는 거리
# 정북방향 0 | 0 <= weak <= n - 1| 1 <= dist <= 8
from itertools import permutations

def solution(n, weak, dist) :
	# 길이를 2배로 늘려서 '원형'을 일자 형태로 변경
	length = len(weak)
	for i in range(length) :
		weak.append(weak[i] + n)
	answer = len(dist) + 1
	# 0부터 length - 1 까지의 위치를 각각 시작점으로 설정
	for start in range(length) :
		# 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
		for friends in list(permutations(dist, len(dist))) :
			count = 1 # 투입할 친구 수
			# 해당 친구가 점검할 수 있는 마지막 위치
			position = weak[start] + friends[count - 1]
			# 시작점부터 모든 취약 지점을 확인
			for index in range(start, start + length) :
				# 점검할 수 있는 위치를 벗어나는 경우
				if position < weak[index] :
					count += 1 # 새로운 친구 투입
					if count > len(dist) : # 더 투입이 불가능하다면 종료
						break
					position = weak[index] + friends[count - 1]
			answer = min(answer, count)
	if answer > len(dist) :
		return -1
	return answer

# 다음 회독 땐 이해할 수 있길..