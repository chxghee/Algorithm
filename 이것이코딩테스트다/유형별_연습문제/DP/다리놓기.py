# https://www.acmicpc.net/problem/1010
import sys
import math
input = sys.stdin.readline

t = int(input())

def cal_result(n,m):
    return math.comb(m,n)


for i in range(t):
    n, m = map(int, input().split())
    print(cal_result(n, m))

