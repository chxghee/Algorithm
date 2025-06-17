# https://www.acmicpc.net/problem/2512
# 떡볶이 문제와 비슷한 문제 (최적값 찾기)

import sys
input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
budget = int(input())

min_budget = budget // n
max_budget = max(req)

result = min_budget
while min_budget <= max_budget:

    mid = (min_budget + max_budget) // 2

    # 현재 상한 예산적용시 남는 금액 계산
    total = 0
    for val in req:
        if val < mid:
            total += val
        else:
            total += mid
    
    if total > budget:
        max_budget = mid -1
    else:
        result = mid
        min_budget = mid + 1
    
print(result)
