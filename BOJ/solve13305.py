# 다시 풀기!!! (58점 코드)

import sys

city_cnt = int(input())
distance_list = list(map(int, input().split()))
oil_cost_list = list(map(int, input().split()))
min_sum = 0

del oil_cost_list[len(oil_cost_list) - 1]


while oil_cost_list :
	min_index = oil_cost_list.index(min(oil_cost_list))
	min_sum +=  oil_cost_list[min_index] * sum(distance_list[min_index :])
	del oil_cost_list[min_index : ]
	del distance_list[min_index : ]

print(min_sum)


### 100점 코드 작성하기

total_cost = 0
min_value = oil_cost_list[0]
for i in range(city_cnt - 1) :
    if oil_cost_list[i] < min_value :
        min_value = oil_cost_list[i]
    total_cost += min_value * distance_list[i]

print(total_cost)