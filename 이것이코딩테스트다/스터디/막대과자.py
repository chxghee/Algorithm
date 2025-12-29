# https://www.acmicpc.net/problem/14219
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

# 3 x 2 / 1x 3
# 둘 중 하나는 반드시 3의 배수 여야 함 = 넓이가 3의 배수이면 됨
if (n * m) % 3 == 0:
    print("YES")
else:
    print("NO")
