# my solve
n = int(input())
coin_cnt = 0

if n >= 500 :
    coin_cnt = int(n / 500)
    n = int(n % 500)

if n >= 100 :
    coin_cnt += int(n / 100)
    n = int(n % 100)

if n >= 50 :
    coin_cnt += int(n / 50)
    n = int(n % 50)

if n >= 10 :
    coin_cnt += int(n / 10)
    n = int(n % 10)

print(coin_cnt)