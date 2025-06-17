# https://www.acmicpc.net/problem/1300

import sys
input = sys.stdin.readline


def count(x):
    cnt = 0
    for i in range(1 , n+1):
        cnt += min(x// i, n)
    return cnt

n = int(input())
k = int(input())

start = 1
end  = k

result = 0
while start <= end:
    mid  = (start + end) // 2

    if count(mid) >= k:
        result = mid
        end = mid -1
    else:
        start = mid + 1

print(result)


# 1. 어떤 값을 찾는데 주어진 제안 시간이 짧다 -> 이분탐색?
# 2. 그러면 탐색의 범위를 생각해 보자 -> 찾는 값의 범위는 1 ~ k 이다 
# 3. 어떻게 해당 값이 찾는값인지 알 수 있을까? -> 해당 값 이전의 값의 개수를 파악해 보자