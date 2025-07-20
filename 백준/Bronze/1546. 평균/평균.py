N = int(input())
s = list(map(int, input().split())) 

m = max(s)
a = sum([(score / m) * 100 for score in s]) / N

print(f"{a:.3f}") 
