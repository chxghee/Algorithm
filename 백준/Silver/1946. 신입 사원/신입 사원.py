# https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

def find_recurit(applicant):
    cnt = 0
    applicant.sort()
    second_min = applicant[0][1]
    
    for i in range(n):
        if second_min >= applicant[i][1]:
            cnt += 1
            second_min = applicant[i][1]


    return cnt


t = int(input())
for _ in range(t):
    n = int(input())
    applicant = []
    for i in range(n):
        x, y = map(int, input().split())
        applicant.append((x,y))
    print(find_recurit(applicant))
