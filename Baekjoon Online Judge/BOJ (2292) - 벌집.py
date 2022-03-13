# Link: https://www.acmicpc.net/source/40994663

n = int(input())

# 지나가야하는 방의 개수
cnt = 1
# 몇 번 째 방
room = 1

while n > room:
    # 최소로 지나가야 하는 방의 개수가 증가할 수록 해당 방의 개수는 6의 배수로 증가
    room += 6 * cnt
    cnt += 1

print(cnt)
