# Link: https://www.acmicpc.net/source/41066618

# 대소문자 구분하지 않으나, 대문자로 출력하기에 .upper()로 받음
word = input().upper()
# 각 알파벳 개수 저장용 리스트
alpha = [0 for i in range(26)]

# 각 알파벳 개수 구하기
for c in word:
    # alpha 리스트의 인덱스 값
    idx = ord(c) - ord('A')
    alpha[idx] += 1

# 중복된 max가 있는지 확인하기
isOverlap = False
max_value = 0
letter = ''
for j, is_max in enumerate(alpha):
    if max_value == is_max:
        isOverlap = True
    elif max_value < is_max:
        isOverlap = False
        max_value = is_max
        # max값을 가지고 있는 문자
        letter = chr(ord('A') + j)

# 정답 프린트하기
if isOverlap:
    print('?')
else:
    print(letter)

# Solution 2

# word,list = input().lower(),[]
# for i in range(97,123):
    # list 기준 알파벳 카운트
#     list.append(word.count(chr(i)))
# print('?'if list.count(max(list))>1 else chr(list.index(max(list))+97).upper())

