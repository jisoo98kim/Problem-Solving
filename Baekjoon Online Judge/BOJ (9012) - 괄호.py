# Link: https://www.acmicpc.net/source/38555516

T = int(input())        # num. of test data

for i in range(T):
    test_case = list(input())
    result = 0      # the print statement depends on this value

    for j in test_case:
        if j == "(": #
            result += 1
        elif j == ")":
            result -= 1
        if result < 0:      # INVALID VPS
            print("NO")
            break

    if result > 0:      # INVALID VPS
        print("NO")
    elif result == 0:       # the only case of VPS
        print("YES")
