while 1 :
  a, b, c = map(int, input().split())

  if a == b == c == 0 :
    break

  large_num = max(a, b, c)

  if large_num == a :
    two_num = b ** 2 + c ** 2
  elif large_num == b :
    two_num = a ** 2 + c ** 2
  else :
    two_num = a ** 2 + b ** 2
  
  if large_num ** 2 == two_num :
    print("right")
  else :
    print("wrong")

