# https://www.acmicpc.net/problem/8394
import sys
input = sys.stdin.readline



# 1번이 악수하는 경우 / 안하는 경우로 나누기

# 1번이 악수하는 경우 -> 1번 제외 N-1 명이 악수
# 2번이 악수하는 경우 -> 1,2번 제외 N-2 명이 악수
n = int(input())


a = 1
b = 2

for i in range(3, n+1):
    tmp = b
    b = (a + b) %10
    a = tmp % 10


if n == 1:
    print(1)
    exit(0)

print(b)

