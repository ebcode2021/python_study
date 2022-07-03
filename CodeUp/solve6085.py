w, h, b = map(int, input().split())

solve = round(w*h*b/8/1024/1024,2)
print("{:0.2f} MB".format(solve))