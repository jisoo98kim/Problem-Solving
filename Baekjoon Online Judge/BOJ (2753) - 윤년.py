#Link: https://www.acmicpc.net/source/39059993

# Checking if the input is a leap year
year = int(input())

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):  # using the remainder operator to check conditions
    print('1')
else:
    print('0')
