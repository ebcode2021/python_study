import math

go, back, height = map(int, input().split())
one_step = go - back

day = (height - back) / one_step
print(math.ceil(day))
