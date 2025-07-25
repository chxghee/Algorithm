import sys
input = sys.stdin.readline

def check():
    # 사다리 타고 결과 확인
    for start in range(1, n + 1):
        pos = start
        for row in range(1, h + 1):
            if ladder[row][pos]:
                pos += 1
            elif ladder[row][pos - 1]:
                pos -= 1
        if pos != start:
            return False
    return True

def dfs(depth, x, y):
    global answer

    # 가지치기
    if depth >= answer or depth > 3:
        return

    # 정답 확인
    if check():
        answer = depth
        return

    # 사다리 추가 탐색
    for i in range(x, h + 1):
        k = y if i == x else 1
        for j in range(k, n):
            # 설치 가능 확인 (현재, 왼쪽, 오른쪽 모두 비어야 함)
            if not ladder[i][j] and not ladder[i][j - 1] and not ladder[i][j + 1]:
                ladder[i][j] = True
                dfs(depth + 1, i, j + 2)  # 오른쪽 인접은 건너뜀
                ladder[i][j] = False

# 입력 처리
n, m, h = map(int, input().split())
ladder = [[False] * (n + 1) for _ in range(h + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    ladder[a][b] = True

answer = 4
dfs(0, 1, 1)
print(answer if answer < 4 else -1)