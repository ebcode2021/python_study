n = int(input())

index = 0
max_index = n - 1
res = 0

list_member = list(map(int, input().split()))
list_member.sort()
list_member.reverse()

while index <= max_index :
    index += list_member[index]
    if index <= max_index + 1 :
        res += 1

print(res)
