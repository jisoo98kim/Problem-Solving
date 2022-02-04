# Link: https://www.acmicpc.net/source/38559342

first = int(input())    # 1st line
second = input()    # 2nd line

three = first * int(second[2])  # 3rd line
four = first * int(second[1])   # 4th line
five = first * int(second[0])   # 5th line

six = first * int(second)   # result of the calculation

print(three, four, five, six, sep='\n') # Use sep to print in new line
