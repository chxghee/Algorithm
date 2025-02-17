# 숫자카드게임
n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    row_min = min(data)

    if result < row_min:
        result = row_min


print(result)

