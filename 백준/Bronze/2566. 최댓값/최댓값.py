import sys
input = sys.stdin.readline
max=0
row=1
col=1
for i in range(9):
    row_data = list(map(int,input().split()))
    for l in range(9):
        current_value = row_data[l]

        if current_value > max:
            max = current_value

            row= i + 1
            col= l+1

    
print(max)
print(row,col)
