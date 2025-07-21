import sys
input = sys.stdin.readline

x=int(input())

for _ in range(x):
    y=int(input()) # 입력값, 센트 단위

    quarter = y // 25
    y %= 25

    dime = y // 10
    y %=10

    nickel = y // 5
    y %= 5

    penny = y

    print(quarter, dime, nickel, penny)