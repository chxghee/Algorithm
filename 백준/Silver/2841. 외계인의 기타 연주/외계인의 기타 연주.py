# https://www.acmicpc.net/problem/2841
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
stack = [[] for _ in range(7)]

count = 0

for _ in range(n):
    line, prat = map(int, input().split())

    if not stack[line]: #비어 있으면
        stack[line].append(prat)
        count += 1
    else:
        top = stack[line][-1]

        if top == prat:
            continue
        elif top < prat:
            stack[line].append(prat)
            count += 1
        else:
            flag = 0
            while True:
                stack[line].pop()
                count += 1
                
                if not stack[line]: #비어 있으면
                    break

                if stack[line][-1] < prat:
                    break

                elif stack[line][-1] == prat:
                    flag = 1
                    break

            if flag == 1:
                continue

            stack[line].append(prat)
            count += 1
            
            
print(count)
