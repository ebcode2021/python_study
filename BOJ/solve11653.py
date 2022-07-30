n = int(input())
num = 2

if n >= 2 :
    while n >= 2 :
        if n % num == 0 :
            n /= num
            print(num)
            num = 2
        else :
            num += 1
else :
    pass

# another solve
v = int(input())
i = 2

while v!= i :
    if v % i == 0 :
        v /= i
        print(i)
    else :
        i += 1