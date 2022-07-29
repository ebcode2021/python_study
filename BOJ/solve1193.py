num = int(input())
line = 1

## 각 line 에는 num 개의 숫자가 포함되어 있음
while num > line :
    num -= line
    line += 1

## 분자가 오름차순
if line % 2 == 0 :
    front = num
    back = line - num + 1
## 분자가 내림차순
elif line % 2 == 1 :
    front = line - num + 1
    back = num

print (str(front) + "/" + str(back))