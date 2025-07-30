# https://www.acmicpc.net/problem/13458
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())


result = 0

for val in a:
    val -= b
    if val <= 0:
        result += 1
        continue

    sub = val // c
    if val % c != 0:
        sub += 1

    result += sub + 1

print(result)