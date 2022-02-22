#Link: https://www.acmicpc.net/source/40412015

# Solution 1: Set
num_list = set()                # 집합에서 중복되는 요소를 제거하기 위해 사용하는 필터
for __ in range(10):
    N = int(input())
    num_list.add(N % 42)        # 집합에 원소를 추가할 때 .add()를 사용해준다

print(len(num_list))            # 중복되는 요소를 제거해서, 몇 개가 다른지 구한다

# Solution 2: List -> Set
"""
num_list = []
for __ in range(10):
    N = int(input())
    num_list.append(N % 42)
num_list = set(num_list)

print(len(num_list))
"""
