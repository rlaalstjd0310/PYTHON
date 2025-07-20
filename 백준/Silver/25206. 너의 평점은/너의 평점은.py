k={"A+":4.5 , "A0":4.0 , "B+" :3.5, "B0":3.0, "C+":2.5,"C0":2.0, "D+":1.5, "D0" :1.0, "F":0.0}
x=0
y=0   
for i in range(20):
    a,b,c=input().split()
    b=float(b)

    if c == "p":
        continue
    if c in k:
        x+=b*k[c]
        y+=b

if y > 0:
    print(f"{x / y:.6f}")  
else:
    print("0.000000")    
