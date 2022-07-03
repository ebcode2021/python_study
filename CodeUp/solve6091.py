a, b, c = map(int, input().split())
cnt = 1

while True :
  if cnt % a == 0 and cnt % b == 0 and cnt % c == 0 :
    break
  cnt += 1

print(cnt)