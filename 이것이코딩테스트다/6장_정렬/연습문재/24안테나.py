# https://www.acmicpc.net/problem/18310
# 문제를 보면 결과값이 나오는 패턴을 분석해 보자

import sys
n = int(sys.stdin.readline().rstrip())
home = list(map(int, sys.stdin.readline().split()))

count = [0] * (max(home) + 1)

for val in home:
    count[val] += 1

result = []
for i in range(len(count)):
    for j in range(count[i]):
        result.append(i)

print(result[(n-1)//2])