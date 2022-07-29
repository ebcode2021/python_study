case = int(input())

person = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
sum = 0

for _ in range(case) :
    a = int(input())
    b = int(input())
    person = [ x for x in range(1, b + 1)]
    for i in range(a) :
        for j in range(1, b) :
            person[j] += person[j - 1]
    print(person[-1])

