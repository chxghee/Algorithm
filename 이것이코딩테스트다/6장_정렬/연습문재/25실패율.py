import sys
stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5


# 현재 a 스테이지인 사람 / a스테이지를 통과한 사람

def solution(N, stages):

    count = [0] * (N + 2)
    
    for i in range(len(stages)):    # 몇번 스테이지에서 막힌 사람 수
        count[stages[i]] += 1

    rate = []
    total_player = len(stages)

    for i in range(1, N+1):
        
        if total_player == 0:
            r = 0
        else:
            r = count[i] / total_player
        rate.append((i, r))
        total_player -= count[i]


    rate.sort(key=lambda x: (-x[1],x[0]))
    
    answer = [val[0] for val in rate]

    return answer

print(solution(N, stages))
