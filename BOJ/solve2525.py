a, b = map(int, input().split())
c= int(input())

total_min = a * 60 + b + c

if total_min >= 60 * 24 :
  total_min %= 60 * 24

c = int(total_min / 60)
d = int(total_min % 60)

print(c, d)