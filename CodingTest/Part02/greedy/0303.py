n , m = map(int, input().split())
new_list = []

tmp = n
while n :
    new_list.append(list(map(int, input().split())))
    n -= 1

n = tmp
while n :
    new_list[n-1].sort()
    n -= 1

max_value = new_list[0][0]
n = tmp

while n :
    if max_value < new_list[n-1][0] :
        max_value = new_list[n-1][0]
    n -= 1

print(max_value)