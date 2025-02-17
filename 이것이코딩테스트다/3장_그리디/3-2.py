# 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

i = 0
result1 = 0

# sol 1
while i < m:

    for _ in range(k):
        if i == m:
            break
        result1 += first
        i += 1
    if i == m: 
        break
    result1 += second
    i += 1

print(result1)   

# sol 2

# first 가 더해지는 횟수
count = m // (k+1)*k + m%(k+1)

# second 가 더해지는 횟수
count2 = m -count

result2 = count*first + count2*second

print(result2)