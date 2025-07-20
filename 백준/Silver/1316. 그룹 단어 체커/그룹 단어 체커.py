t = int(input()) 
k = 0 

for i in range(t):
    word = input()
    x = ' ' 

    for z in word:
        if not x or x[-1] != z:  
            x += z  

    if len(set(x)) == len(x):
        k += 1

print(k)
