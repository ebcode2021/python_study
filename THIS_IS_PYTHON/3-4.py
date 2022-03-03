n, k = map(int, input().split())

count = 0

while(n != 1):
    if(n % k != 0):
        n -= 1
    else:
        n //= k

    count += 1

print(count)

# 다른 풀이1
n, k = map(int, input().split())

count = 0

while n>=k :
    while n % k != 0 :
        n -= 1
        count += 1
    n //= k
    count += 1

while n > 1 :
    n -= 1
    count += 1

print(count)


# 다른 풀이2
n, k = map(int, input().split())

count = 0

while True :
    target = (n//k)*k
    count += (n-target)
    n = target

    if n< k :
        break
    count += 1
    n //= k

    count +=(n-1)
    print(count)