# https://www.acmicpc.net/problem/10825
# 정렬 기본 예제 - 람다식으로 여러 기준 설정 

import sys


n = int(sys.stdin.readline().rstrip())
data = []

for i in range(n):
    stu, kor, eng, math = sys.stdin.readline().split()
    s = [stu, int(kor), int(eng),int(math)]
    data.append(s)

print(data)

result = sorted(data, key=lambda x: (-x[1],x[2],-x[3],x[0]))


for val in result:
    print(val[0])