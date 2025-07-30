# https://www.acmicpc.net/problem/14890
import sys
input = sys.stdin.readline


# 순회 하면서 flag 값을 둔다
# 현재 - 오른쪽 = 0 -> 진행 가능
# 현재 - 오른쪽 = -1 -> 왼쪽 칸이 L 만큼 자리가 있는지
# 현재 - 오른쪽 = 1  -> 오른쪽 칸이 L 만큼 자리가 있는지 



def find(data):
    result = 0
    for i in range(n):
        flag = 0
        used = [False] * n
        for j in range(n-1):
            now = data[i][j]
            nxt = data[i][j+1]

            diff = now - nxt

            if diff == 0:
                continue

            elif diff == -1:
                for k in range(l):
                    back = j - k
                    if back < 0 or data[i][back] != now or used[back]:
                        flag = 1
                        break
                if flag == 1:
                    break
                
                for k in range(l):
                    back = j - k
                    used[back] = True
                    

            
            elif diff == 1:
                for k in range(l):
                    foward = j + 1 + k
                    if foward >= n or data[i][foward] != nxt or used[foward]:
                        flag = 1
                        break
                if flag == 1:
                    break
                
                for k in range(l):
                    foward = j + 1 + k
                    used[foward] = True
                
                
            else:
                flag = 1
                break
        
        if flag == 0:
            result += 1
    return result


n, l = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
data2 = []

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(data[j][i])
    data2.append(tmp)

result = find(data) + find(data2)

print(result)
