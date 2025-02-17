# 동전 https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

result = 0


for c in reversed(coin):
    
    result += k // c
    k %= c

print(result)
    