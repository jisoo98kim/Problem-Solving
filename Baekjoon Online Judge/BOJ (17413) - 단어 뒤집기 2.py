# Link: https://www.acmicpc.net/source/40953036

str = list(input())
flag = False
word = ''
ans = ''

for idx in str:
    # print reversely
    if flag == False:
        if idx == '<':
            flag = True
            # add '<' to word
            word += idx
            continue

        elif idx == ' ':
            word += idx
            ans += word
            # reset the word
            word = ''
            continue

        else:
            # print the saved word reversely
            word = idx + word
            continue

    # print the original
    elif flag:
        # add the word after '<' originally until we meet '>'
        word += idx
        if idx == '>':
            flag = False
            # add the word between '<' and '>' as original into the ans
            ans += word
            # reset the word
            word = ''

print(ans + word)

