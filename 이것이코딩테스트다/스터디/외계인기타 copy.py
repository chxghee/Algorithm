# https://www.acmicpc.net/problem/2841
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
stack = [[] for _ in range(7)]

count = 0
i = 0
while i < n:

    line, prat = map(int, input().split())

    if not stack[line]: #비어 있으면
        stack[line].append(prat)
        count += 1
    else:
        top = stack[line][-1]

        if top < prat:
            stack[line].append(prat)
            count += 1
        elif top > prat:
            stack.pop()
            count += 1
            continue

    i += 1



print(count)

