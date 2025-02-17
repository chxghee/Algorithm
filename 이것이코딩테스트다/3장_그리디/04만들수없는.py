import sys

n = int(sys.stdin.readline())
coin = list(map(int, sys.stdin.readline().split()))
coin.sort()
result = 1

for x in coin:
    if result < x:
        break
    result += x

print(result)
