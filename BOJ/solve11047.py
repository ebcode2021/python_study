n, m = map(int, input().split())
coin_list = []
coin_cnt = 0

for _ in range(n) :
    coin_list.append(int(input()))
coin_list.reverse()

for coin in coin_list :
    if m == 0 :
        break
    if m // coin != 0 :
        coin_cnt += m // coin
        m %= coin

print(coin_cnt)

""" 시간 초과 코드
for coin in coin_list :
    while m // coin != 0 :
        coin_cnt += 1
        m -= coin
"""