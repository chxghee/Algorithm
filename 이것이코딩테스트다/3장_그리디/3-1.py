# 거스름돈
n = int(input())

coin_types = [500, 100 ,50 ,10]
result = []

for x in coin_types:
    result.append(n // x)
    n = n % x

print(result)