# https://www.acmicpc.net/problem/1654

# 이진 탐색같은 느낌이 드는데, 최적의 해를 찾아야 한다 
# -> 종료조건 없는 while문을 통해 최적의 해를 갱신하며 찾기

import sys
input = sys.stdin.readline


def possible_lan_cnt(line, length):
    lan_cnt = 0

    for val in line:
        lan_cnt += val // length

    return lan_cnt
    

k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))

# 일단 가장 최대 = 총합 / n  이다
end = sum(line) // n
start = 1


result = 0
while start <= end:
    mid = (start + end) // 2

    lan_cnt =  possible_lan_cnt(line, mid)

    if lan_cnt < n:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)


