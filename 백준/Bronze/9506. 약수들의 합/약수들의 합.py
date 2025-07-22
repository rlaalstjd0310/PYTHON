import sys
input = sys.stdin.readline

while True:
    x = int(input())
    if x == -1:
        break


    list=[]
    for i in range(1,x):
        if x%i == 0:
            list.append(i)

    if sum(list) == x:
        print(f"{x} = {' + '.join(map(str,list))}")
    else :
        print(f"{x} is NOT perfect.")
