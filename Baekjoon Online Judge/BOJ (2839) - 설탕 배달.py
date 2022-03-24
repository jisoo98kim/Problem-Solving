# Link: https://www.acmicpc.net/source/41107018

n = int(input())

cnt = 0
while n >= 0:
     if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
     # 5의 배수가 되기 전까지는 -3 kg, 봉지 수 + 1
     n -= 3
     cnt += 1
# n이 0이 될 때까지 5의 배수로 나누어 떨어지지 않을 경우
else:
    print(-1)
