# https://www.acmicpc.net/problem/1744
import sys
input = sys.stdin.readline

n = int(input())
positive = []
negative = []

def calculate_p(arr):
    r = 0
    if len(arr) % 2 != 0:
        r = arr.pop()

    while arr:

        n1 = arr.pop()
        n2 = arr.pop()

        if n1 == 1:
            r += n1 + n2
        else:
            r += n1 * n2

    return r

def calculate_n(arr):
    r = 0
    if len(arr) % 2 != 0:
        r = arr.pop()

    while arr:

        n1 = arr.pop()
        n2 = arr.pop()
        r += n1 * n2

    return r


for i in range(n):
    d = int(input())
    if d > 0:
        positive.append(d)
    else:
        negative.append(d)

positive.sort(reverse=True)
negative.sort()

r1 = calculate_p(positive)
r2 = calculate_n(negative)

print(r1 + r2)