# https://www.acmicpc.net/problem/29717
import sys
input = sys.stdin.readline



# 레벨을 기준으로 이분탐색
def binary_search(start, end, target):
    global result

    if start > end:
        return
    
    mid = (start + end) // 2
    exp = mid ** 2 + mid

    if exp < target:
        start = mid + 1
        binary_search(start, end, target)
    else:
        result = mid
        end = mid - 1
        binary_search(start, end, target)
    


t= int(input())

for _ in range(t):
    n = int(input())
    
    start = 0
    end = n         # 최종레벨은 절대 n을 넘을 수 없음
    target = (n**2 + n) // 2
    result = 0
    
    binary_search(start, end, target)
    
    print(result)






    



# 2 4 6 8 10 -> L 레벨 도달하기 위한 경험치 = L(L-1)

# 1 2 3 4 5 6 7 8 9 10 -> n마리를 잡았을 때 얻는 경험치 = n(n+1) // 2


