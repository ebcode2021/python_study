#바둑알 깔기
my_lists = []
for i in range(19) :
  input_list = input().split()
  mapped_int_list = list(map(int, input_list))
  my_lists.append(mapped_int_list)
#for item in my_list:
 # print(item)

# 십자 뒤집기 횟수(n)
n = int(input())
for loop in range(n) :
  x, y = map(int, input().split())

  for i in range(19) :
    
    my_lists[x-1][i] = int(not my_lists[x-1][i])
    '''
    if my_lists[x-1][i] == 1 :
      my_lists[x-1][i] = 0
    else :
      my_lists[x-1][i] = 1

    '''
    my_lists[i][y-1] = int(not my_lists[i][y-1] )
    '''
    if my_lists[i][y-1] == 1 :
      my_lists[i][y-1] = 0
    else : 
      my_lists[i][y-1] = 1
    '''
'''
for i in range(19) :
  for j in range(19) :
    print(my_list[i][j], end=" ")
  print()
'''
for row in my_lists:
  for item in row:
    print(item, end=' ')
  print()
