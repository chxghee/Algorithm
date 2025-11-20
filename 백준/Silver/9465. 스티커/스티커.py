# https://www.acmicpc.net/problem/9465
import sys
input = sys.stdin.readline

def check_range(c, idx):
    return 0 <= idx < c


def get_point(dp, idx_tuple):
    x, y = idx_tuple
    if not check_range(len(dp[0]), y):
        return 0
    return dp[x][y]

# 자신의 대각 이전, 2칸 뛰고 이전 이랑 비교
def result(sticker, c):
    dp = [[0] * c for _ in range(2)]

    for j in range(c):
        for i in range(2):
            now = sticker[i][j]

            x = ((i+1) % 2, j - 1)
            y = (i, j - 2)
            z = ((i+1) % 2, j - 2)

            max_point = max(get_point(dp, x), get_point(dp, y), get_point(dp, z))

            dp[i][j] = max_point + now

    return max(dp[0][c-1], dp[1][c-1])

n = int(input())

for _ in range(n):
    c = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    print(result(sticker, c))

