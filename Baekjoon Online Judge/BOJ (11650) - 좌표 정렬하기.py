# Link: https://www.acmicpc.net/source/38501363

N = int(input())
arr = [] # create an empty list

# Collect numbers into the list "arr"
for i in range(N):
    x, y = map(int, input().split(' '))
    arr.append([x, y])
arr.sort() # sort the list in ascending order

for i in range(N):
    print(arr[i][0], arr[i][1])
