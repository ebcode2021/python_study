n, m, k = map(int, input().split())

result = 0
input_list = list(map(int, input().split()))
input_list.sort()
input_list.reverse()

one_group = input_list[0] * k + input_list[1]

result = one_group * (m // (k + 1)) + input_list[0] * (m % (k + 1))
print(result)

