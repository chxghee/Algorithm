# ATM https://www.acmicpc.net/problem/11399

n = int(input())
data = list(map(int, input().split()))

result =0
data.sort()
w = 0
for t in data:
    w += t
    result += w

print(result)