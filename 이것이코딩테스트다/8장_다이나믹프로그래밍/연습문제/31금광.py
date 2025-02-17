import sys

# 금광 데이터를 2차원 배열로 만들기
def mine():
    gold = []
    col = 0
    for i in range(n):
        gold.append(data[col:col+m])
        col += m
    return gold


# 채굴할 수 있는 인접 광산중 큰 값 구하기
def find_adj_max(x,y):
    
    if x == 0:
        left_up = 0
    else:
        left_up = gold[x-1][y-1]

    left = gold[x][y-1]

    if x == n-1:
        left_down = 0
    else:
        left_down = gold[x+1][y-1]
    
    return max(left_up, left, left_down)


# 찾기 현재 위치의 dp값을 이전 위치의 최대 값을 더해서 갱신하기
def find():
    dp = gold
    
    for i in range(1, m):
        for j in range(n):

            dp[j][i] = dp[j][i] + find_adj_max(j, i)

    result = [dp[i][m-1] for i in range(n)]
    
    return max(result)


t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    gold = mine()
    print(find())
    






# 1
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7