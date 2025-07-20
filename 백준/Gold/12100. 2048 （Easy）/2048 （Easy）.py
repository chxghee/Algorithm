# https://www.acmicpc.net/problem/12100
import sys
import copy
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]


def find_max_num(data):
    result = 0
    for i in range(n):
        tmp = max(data[i])
        result = max(result, tmp)
    return result

def move_position(data, dirc):

    d = copy.deepcopy(data)

    if dirc == 0:  # 오른쪽
        for i in range(n):
            pivot = d[i][n-1]
            p_idx = n-1
            for j in range(n-2, -1, -1):        

                if pivot != 0:      # 기준점 0 아니고
                    if d[i][j] != 0:    # 비교값이 0 아니면
                        if pivot == d[i][j]: # 같은 값이라면 합치기
                            d[i][j] = 0
                            pivot *= 2

                            d[i][p_idx] = pivot
                            p_idx -= 1
                            pivot = 0

                        else:                # 다른 값이면 pivot 한 칸 이동 
                            d[i][p_idx] = pivot
                            p_idx -= 1
                            pivot = d[i][j]
                            d[i][j] = 0
                        
                    

                else:       # 현재 pivot 이 0 이면 값을 당겨와야 한다는 것
                    if d[i][j] != 0:
                        pivot = d[i][j]
                        d[i][j] = 0
            
            
            d[i][p_idx] = pivot         # pivot 값 반영
        

    elif dirc == 1:  # 아래
        for i in range(n):
            pivot = d[n-1][i]
            p_idx = n-1
            for j in range(n-2, -1, -1):    
                

                if pivot != 0:      # 기준점 0 아니고
                    if d[j][i] != 0:    # 비교값이 0 아니면
                        if pivot == d[j][i]: # 같은 값이라면 합치기
                            d[j][i] = 0
                            pivot *= 2

                            d[p_idx][i] = pivot
                            p_idx -= 1
                            pivot = 0


                        else:                # 다른 값이면 pivot 한 칸 이동 
                            d[p_idx][i] = pivot

                            p_idx -= 1
                            pivot = d[j][i]
                            d[j][i] = 0
                            
                    

                else:       # 현재 pivot 이 0 이면 값을 당겨와야 한다는 것
                    if d[j][i] != 0:
                        pivot = d[j][i]
                        d[j][i] = 0
            
                d[p_idx][i] = pivot         # pivot 값 반영


    elif dirc == 2:   # 왼
        for i in range(n):
            pivot = d[i][0]
            p_idx = 0
            for j in range(1, n):    
                

                if pivot != 0:      # 기준점 0 아니고
                    if d[i][j] != 0:    # 비교값이 0 아니면
                        if pivot == d[i][j]: # 같은 값이라면 합치고 피봇 이동(합친건 다시 합칠 수 없음)
                            d[i][j] = 0
                            pivot *= 2
                            
                            d[i][p_idx] = pivot
                            p_idx += 1
                            pivot = 0
                            

                        else:                # 다른 값이면 pivot 한 칸 이동 
                            d[i][p_idx] = pivot
                            p_idx += 1
                            pivot = d[i][j]
                            d[i][j] = 0

                else:       # 현재 pivot 이 0 이면 값을 당겨와야 한다는 것
                    if d[i][j] != 0:
                        pivot = d[i][j]
                        d[i][j] = 0
            
                d[i][p_idx] = pivot         # pivot 값 반영
        
        
    else:       # 위
        for i in range(n):
            pivot = d[0][i]
            p_idx = 0
            for j in range(1, n):    
                

                if pivot != 0:      # 기준점 0 아니고
                    if d[j][i] != 0:    # 비교값이 0 아니면
                        if pivot == d[j][i]: # 같은 값이라면 합치기
                            d[j][i] = 0
                            pivot *= 2

                            d[p_idx][i] = pivot
                            p_idx += 1
                            pivot = 0

                        else:                # 다른 값이면 pivot 한 칸 이동 
                            d[p_idx][i] = pivot
                            p_idx += 1
                            pivot = d[j][i]
                            d[j][i] = 0
                            
                    

                else:       # 현재 pivot 이 0 이면 값을 당겨와야 한다는 것
                    if d[j][i] != 0:
                        pivot = d[j][i]
                        d[j][i] = 0
            
                d[p_idx][i] = pivot         # pivot 값 반영

    return d
    


def lv(data, depth):
    
    if depth == 5:
        return find_max_num(data)


    results = []
    for i in range(4):
        new_d = move_position(data, i)
        results.append(lv(new_d, depth+1))

    return max(results)

print(lv(data, 0))

        

"""
5
0 0 128 0 8
64 0 0 2 2
2 8 0 0 64
2 32 4 8 8
0 0 0 16 0

256

4
32 64 0 0
4 128 256 0
128 4 16 2
4 128 32 32

256


4
2 2 4 16
0 0 0 0
0 2 0 2
0 0 0 0


3
2 2 2
0 0 0
0 0 0

"""