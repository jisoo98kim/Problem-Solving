# Link: https://www.acmicpc.net/source/40529031

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']     # set croatia alphabet list
test = input()

for i in croatia:
    test = test.replace(i, '*')                                 # change croatia alphabet to length 1 with '*'

print(len(test))                                                # print length of test
