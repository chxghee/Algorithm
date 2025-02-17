# 
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

def find_least_dist():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    distance = [[INF] * n for _ in range(n)]

    q = []

    # 현재 에너지 정보와 (좌표)를 힙에 삽입
    heapq.heappush(q, (data[0][0], (0,0)))
    distance[0][0] = data[0][0]

    while q:
        dist, position = heapq.heappop(q)
        x = position[0]
        y = position[1]

        if dist > distance[x][y]:
            continue

        for i in range(4):

            # 범위를 넘어가는 지 쳌
            if (x + dx[i] < 0 or x + dx[i] >= n) or (y + dy[i] < 0 or y + dy[i] >= n):
                continue

            cost = dist + data[x + dx[i]][y + dy[i]]
            if cost < distance[x + dx[i]][y + dy[i]]:
                distance[x + dx[i]][y + dy[i]] = cost
                heapq.heappush(q, (cost, (x + dx[i], y + dy[i])))

    return distance[n-1][n-1]



t = int(input())

for _ in range(t):
    print(find_least_dist())


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
"""