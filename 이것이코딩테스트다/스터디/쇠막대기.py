# https://www.acmicpc.net/problem/10799
import sys
input = sys.stdin.readline


# (). ( ( (. (). (). ) (())  ()  ))    (())

# 막대 의 괄호 사이에 존재하는 레이저의 개수에 따라 토막이 나뉨 -> 토막 수 = 레이저 개수 + 1
# 1 -> 5개
# 2 -> 5
# 3 -> 3
# 4 -> 2
# 5-> 2


st = input().rstrip()

result = 0
stack = []
i = 0
while i < len(st):
    c = st[i]
    
    if st[i] == '('  and st[i+1] == ')':
        
        result += len(stack)
        i += 2
        continue

    if c == '(':
        stack.append(c)
    else:
        stack.pop() 
        result += 1
    i += 1
    

print(result)