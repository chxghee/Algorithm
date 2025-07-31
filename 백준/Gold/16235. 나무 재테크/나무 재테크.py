from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def is_on_ground_range(x, y):
    return 0 <= x < n and 0 <= y < n

def spring_summer():
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            
            new_trees = deque()
            dead_nutrient = 0
            
            # 나이가 어린 순서대로 처리 (이미 정렬되어 있음)
            while trees[i][j]:
                age = trees[i][j].popleft()
                if ground[i][j] >= age:
                    ground[i][j] -= age
                    new_trees.append(age + 1)
                else:
                    # 양분 부족하면 죽음
                    dead_nutrient += age // 2
                    # 나머지 나무들도 모두 죽음 (나이순이므로)
                    while trees[i][j]:
                        dead_nutrient += trees[i][j].popleft() // 2
                    break
            
            trees[i][j] = new_trees
            ground[i][j] += dead_nutrient

def autumn():
    breed_list = []
    
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            
            # 번식할 나무들 찾기
            breed_count = 0
            for age in trees[i][j]:
                if age % 5 == 0:
                    breed_count += 1
            
            if breed_count > 0:
                for d in range(8):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if is_on_ground_range(nx, ny):
                        breed_list.append((nx, ny, breed_count))
    
    # 새로운 나무들 추가 (나이 1을 앞쪽에 추가)
    for x, y, count in breed_list:
        for _ in range(count):
            trees[x][y].appendleft(1)

def winter():
    for i in range(n):
        for j in range(n):
            ground[i][j] += nutrient[i][j]

# 입력
n, m, k = map(int, input().split())
ground = [[5] * n for _ in range(n)]
nutrient = []
for i in range(n):
    nutrient.append(list(map(int, input().split())))

# 각 칸별로 나무 deque 관리 (정렬된 상태 유지)
trees = [[deque() for _ in range(n)] for _ in range(n)]

# 초기 나무들을 나이순으로 정렬해서 추가
initial_trees = []
for _ in range(m):
    x, y, z = map(int, input().split())
    initial_trees.append((z, x-1, y-1))

initial_trees.sort()
for age, x, y in initial_trees:
    trees[x][y].append(age)

# k년간 시뮬레이션
for year in range(k):
    spring_summer()
    autumn()
    winter()

# 결과 출력
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)