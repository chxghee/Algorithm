import sys

n, m = map(int, sys.stdin.readline().split())
ball = list(map(int, sys.stdin.readline().split()))

array = [0]*11

for x in ball:
    array[x]+=1
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)
