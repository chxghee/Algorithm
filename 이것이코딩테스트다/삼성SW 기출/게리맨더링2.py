# https://www.acmicpc.net/problem/17779

import sys
input = sys.stdin.readline




def is_possible




n = int(input().split())
a = [list(map(int, input().split())) for _ in range(n)]




for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x > n - d1 - d2 or
