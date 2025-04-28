# https://www.acmicpc.net/problem/2437
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

scala = 0
for weight in data:
    if weight > scala + 1:
        print(scala + 1)
        break
    scala += weight

else:
    print(scala + 1)

