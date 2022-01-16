a,b,c = input().split()
A = int(a)
B = int(b)
C = int(c)

print(a) if(A<=B and A<=C) else (print(B) if(B<=C) else print(C))