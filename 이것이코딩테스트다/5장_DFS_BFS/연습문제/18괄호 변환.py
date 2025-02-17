from collections import deque

p1 ="(()())()"	# "(()())()"
p2 = ")("       #	"()"
p3 = "()))((()"	#"()(())()"


def solution(p):
    
    answer = ''
    if p == '':
        return answer
    idx = balance_index(p)    
    u = p[:idx+1]
    v = p[idx+1:]

    if check_right(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        answer += reverse_str(u)

    return answer

        
def reverse_str(p):
    
    new = list(p[1:-1])
    for i in range(len(new)):
        if new[i] == '(':
            new[i] = ')'
        else:
            new[i] = '('
    return "".join(new)
        

def balance_index(p):

    cnt = 0 
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        if p[i] == ')':
            cnt -= 1
        if cnt == 0:
            return i

def check_right(p):
    if len(p) == 0:
        return True
    
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        elif p[i] == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0


def asd(p):
    count = 0
    for i in p:
        if i == '(':
            count +=1
        else:
            if count == 0:
                return False
            count -= 1
    return True


result = solution(p3)

print(result)
