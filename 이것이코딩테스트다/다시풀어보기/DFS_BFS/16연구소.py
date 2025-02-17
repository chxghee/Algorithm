# https://www.acmicpc.net/problem/14502
import sys
input = sys.stdin.readline

# 입력
n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

print(data)