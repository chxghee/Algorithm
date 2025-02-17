import sys
# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = len(s)

    for length in range(1, len(s)//2 + 1):
        result = 0
        cnt = 1
        st = s[0:length]

        for i in range(length, len(s), length):
            cmp = s[i:i+length]
            
            if st == cmp:
                cnt += 1
               
            else:
                if cnt == 1:
                    result += len(st)    
                else:
                    result += len(str(cnt)) + len(st)
                st = cmp
                cnt = 1
                

        if cnt != 1:
            result += len(str(cnt)) + len(st)
        else:
            result += len(st)

 ##      result += len(st) + (len(str(cnt)) if cnt > 1 else 0)
        answer = min(answer, result)
    return answer

s = sys.stdin.readline().rstrip()
print(solution(s))