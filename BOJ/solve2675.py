t = int(input())

while t != 0 :
    r, s = input().split()
    text = ""
    for i in s :
        text += int(r) * i
    print(text)
    t -= 1