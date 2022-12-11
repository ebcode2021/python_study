def buildCheck(build_one, answers) :
	x, y = build_one[0], build_one[1]
	if (build_one[2]) : # 1이면 보
		for answer in answers :
			if (answer[0] == x and answer[1] == y) or (answer[0] == (x + 1) and answer[1] == y) :
				return ([x + 1, y, 1])
	else : # 0이면 기둥
		for answer in answers :
			if (answer[0] == x and answer[1] == y) or y == 0 :
				return ([x, y + 1, 0])
	return (0)

def cancelBeam(x, y) :
	return (0)

def cancelColumn(x, y) :
	return (0)

def cancelCheck(build_one, answers) :
	x, y = build_one[0], build_one[1]
	if build_one[2] :
		return cancelBeam(x - 1, y)
	else :
		return cancelColumn(x, y - 1)

def solution(n, build_frame) :
	answer = [[]]
	for build_one in build_frame :
		if (build_one[3]) :
				answer.append(buildCheck(build_one, answer)) if (buildCheck(build_one, answer)) else 0
		else :
				answer.remove(cancelCheck(build_one, answer)) if (cancelCheck(build_one, answer)) else 0
	answer.sort(key = lambda x : (x[0], x[1], x[2]))
	return answer

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]


# build_frame [x, y, a, b]
"""
	x,y는 설치할 교차점의 시작 좌표
	a -> 0 : 기둥 / a -> 1 : 보
	바닥에 보 설치 x
	b -> 0 : 삭제 / b -> 1 : 설치
"""
# return 배열 [x, y, a]
"""
	x, y 는 설치물의 교차점의 도착 좌표 
	a -> 0 : 기둥 / a -> 1 : 보
"""
