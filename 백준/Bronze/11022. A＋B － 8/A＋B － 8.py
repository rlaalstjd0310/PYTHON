a = int(input())
for i in range(1, a + 1):
    x,y = map(int, input().split())
    z=x+y
    print(f"Case #{i}: {x} + {y} = {z}")