n, k = map(int, input().split())
cnt = 0

tmp = k
while n >= tmp :
    cnt += 1
    tmp *= k

res = k ** cnt

while res != n :
    res += 1
    cnt += 1

print(cnt)
