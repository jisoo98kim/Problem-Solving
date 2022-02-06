# Link: https://www.acmicpc.net/source/39027114

palin = input()

if palin == palin[::-1]:
    print('1')
else:
    print('0')
