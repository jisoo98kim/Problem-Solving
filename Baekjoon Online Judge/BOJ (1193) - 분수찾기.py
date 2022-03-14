# Link: https://www.acmicpc.net/source/41007035

n = int(input())

# 사선 라인
line = 0
# 해당 라인에서 가장 큰 숫자
max_num = 0

# n이 몇 번째 사선라인에 있는지 확인
while n > max_num:
    line += 1
    #
    max_num += line

# 라인 최댓값 - 입력 받은 수
diff = max_num - n

# 짝수 번 째 라인
if line % 2 == 0:
    numer = line - diff         # 분자
    deno = diff + 1             # 분모
# 홀수 번 째 라인
else:
    numer = diff + 1            # 분자
    deno = line - diff          # 분모

print(f'{numer}/{deno}')
