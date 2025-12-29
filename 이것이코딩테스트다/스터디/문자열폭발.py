# https://www.acmicpc.net/problem/9935
import sys
input = sys.stdin.readline

# append하다 마지막 문자열이 같다면 폭발 문자열인지 확인한다.
# 만약 같다면 pop
# 같지 않으면 append


# 폭발 문자열인지 확인한다.
def has_boom(result):
    return ''.join(result[-boom_len:]) == boom


st = input().rstrip()
boom = input().rstrip()
last_c = boom[-1]
boom_len = len(boom)

result = []
for c in st:
    result.append(c)
    
    if c == last_c:
        if has_boom(result):
            for _ in range(boom_len):
                result.pop()
    
        
if result:
    print(''.join(result))
else:
    print("FRULA")
