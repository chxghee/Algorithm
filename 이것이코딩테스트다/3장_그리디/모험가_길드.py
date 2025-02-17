import sys

N = int(sys.stdin.readline())
fear = list(map(int, sys.stdin.readline().split()))

fear.sort()
g = 0
cnt = 0

for data in fear:
    cnt += 1
    if cnt >= data:
        g += 1
        cnt =0


print(g)
