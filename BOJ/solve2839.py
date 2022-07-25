sugar = int(input())

five_bag = sugar // 5
three_bag = (sugar - five_bag * 5) // 3

while (five_bag != 0 or three_bag != 0) and five_bag >= 1:
    if five_bag * 5 + three_bag * 3 == sugar :
        break
    five_bag -= 1
    three_bag = (sugar - five_bag * 5) // 3

if five_bag * 5 + three_bag * 3 == sugar :
    print(five_bag + three_bag)
else :
    print (-1)