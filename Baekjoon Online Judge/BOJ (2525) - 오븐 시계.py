#Link: https://www.acmicpc.net/source/39061734

current_hour, current_min = map(int, input().split(' '))
cooking_time = int(input())

current_time = current_hour * 60 + current_min  # current time in minutes
hour = (current_time + cooking_time) // 60  # set quotient to hour
min = (current_time + cooking_time) % 60    # set remainder to min

if hour >= 24:  # to follow the correct format
    hour %= 24

print(hour, min)
