a,b = input().split()

A = bool(int(a))
B = bool(int(b))
print((A & B) or ((not A) & (not B)))