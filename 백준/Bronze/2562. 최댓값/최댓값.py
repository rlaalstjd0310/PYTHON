c=[]
b=[]
for i in range (9):
    a=int(input())
    b.append(a)
    c.append(a)
b.sort()
print(b[8])
print(c.index(b[8]) + 1)