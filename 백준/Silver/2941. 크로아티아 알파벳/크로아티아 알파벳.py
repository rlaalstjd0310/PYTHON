m = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n = input() 

for i in m:
    n = n.replace(i, '*') 

print(len(n))
