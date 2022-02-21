#link: https://www.acmicpc.net/source/40408391

a = int(input())
b = int(input())
c = int(input())

mult = a * b * c

for i in range(10) :
    print(str(mult).count(str(i)))
