# https://www.acmicpc.net/problem/1789
import sys
input = sys.stdin.readline

s = int(input())
sum_result = 0
cnt = 0
i = 1

while sum_result < s:
    sum_result += i
    i += 1

if sum_result != s:
    i -= 1


print(i - 1)