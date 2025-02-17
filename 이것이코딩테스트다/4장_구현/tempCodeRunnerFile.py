def solution(s):
    answer = len(s)

    for length in range(1, len(s)//2 + 1):
        result = 0
        cnt = 0
        st = s[0:length]

        for i in range(length, len(s), length):
            cmp = s[i:i+length]
            
            if st == cmp:
                cnt += 1
               
            else:
                if cnt == 0:
                    result += len(st)    
                else:
                    result += len(str(cnt)) + len(cmp)
                st = s[i:i+length]
                cnt = 0
                

        if cnt != 0:
            result += len(str(cnt + 1)) + len(cmp)
        else:
            if result == 0:
                result = len(s)
            else:
                result += len(cmp)
                
        if result < answer:
            answer = result

    return answer
