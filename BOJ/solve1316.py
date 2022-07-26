total_cnt = int(input())
word_list = []
res = 0

for _ in range(total_cnt) :
    word_list.append(input())

for word in word_list :
    storage_list = []
    flag = 1
    for i in range(len(word) - 1) :
        if word[i] in storage_list :
            flag = 0
            break
        if word[i] != word[i + 1] :
            storage_list.append(word[i])
    if flag != 0 and word[-1] not in storage_list :
        res += 1

print(res)
