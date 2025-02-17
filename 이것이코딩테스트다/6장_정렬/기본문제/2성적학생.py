n = int(input())

data = []
for i in range(n):
    inp = input().split()
    data.append((inp[0], int(inp[1])))

def setting(d):
    return  d[1]
# 함수 이용
data.sort(key=setting)

# 람다식 이용
data.sort(key=lambda student: student[1]) 

for value in data:
    print(value[0], end=' ')

