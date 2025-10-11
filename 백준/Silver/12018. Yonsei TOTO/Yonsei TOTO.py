# https://www.acmicpc.net/problem/12018

import sys
input = sys.stdin.readline

# 수강인원: l / 신청인원: p
def cal_min_point(point, p, l):

    if l > p:
        return 1

    point.sort(reverse=True)
    
    return point[l-1]


n,m = map(int, input().split())

min_points = []

for i in range(n):
    p ,l = map(int, input().split())
    point = list(map(int, input().split()))
    min_points.append(cal_min_point(point, p, l))

min_points.sort()


result = 0
for val in min_points:
    required_point = val
    
    if m >= required_point:
        m -= required_point
        result += 1
    
    else:
        break

print(result)


