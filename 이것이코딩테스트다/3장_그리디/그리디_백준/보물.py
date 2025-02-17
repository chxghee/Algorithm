# https://www.acmicpc.net/problem/1026
import sys

N = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

result = 0
a.sort()
b.sort(reverse=True)

for i in range(N):
    result += a[i] * b[i]

print(result)


