# https://www.acmicpc.net/problem/2295
import sys
input = sys.stdin.readline

n = int(input())

u = []

for i in range(n):
    u.append(int(input()))

u.sort()
sum_two = set()

for i in range(n):
    for j in range(n):
        sum_two.add(u[i] + u[j])


for i in range(n-1,0,-1):
    for j in range(i+1):
        find = u[i] - u[j]
        if find in sum_two:
            print(u[i])
            sys.exit(0)
