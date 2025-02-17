# https://www.acmicpc.net/problem/1541

n = input()

data = n.split('-')

for i in range(len(data)):
    parts = data[i].split('+')
    # 각 숫자를 int로 변환해 앞의 0을 제거하고 다시 문자열로 변환
    data[i] = '+'.join(str(int(num)) for num in parts)


for i in range(len(data)):
    data[i] = str(eval(data[i]))

result = 0

for i in range(len(data)):
    if i == 0:
        result += int(data[i])
    else:
        result -= int(data[i])

print(result)


# 다른 풀이
n = input()

# '-'로 분리하고 각 부분을 '+' 기준으로 더한 값을 계산
data = [sum(map(int, part.split('+'))) for part in n.split('-')]

# 첫 번째 값에서 나머지 값을 모두 뺌
result = data[0] - sum(data[1:])

print(result)


