a=[]
for i in range(10):
    t=int(input())
    a.append(t%42)

print(len(set(a)))