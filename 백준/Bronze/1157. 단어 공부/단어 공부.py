t = input().upper()
k = set(t)  

x = [t.count(i) for i in k] 
y = max(x) 

if x.count(y) > 1:
    print("?")
else:
    print(list(k)[x.index(y)])
