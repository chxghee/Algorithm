# https://www.acmicpc.net/problem/13305
n = int(input())
d = list(map(int,input().split()))
city = list(map(int,input().split()))

i = 0
cost = 0
fuel = 0

while i < n-1: 

    # 현재위치보다 작은 비용의 가장 가까운 주유소를 찾기
    idx = -1
    for j in range(i+1, n-1):
        if city[i] > city[j]:
            idx = j
            break
    
    # 현재 위치가 가장 싼 주유소
    if idx == -1:
        fuel += sum(d[i:len(d)])
        cost += city[i] * sum(d[i:len(d)])
        break

    else:
        fuel += sum(d[i+1:idx])
        cost += city[i] * sum(d[i:idx])
        i=idx
       

print(cost)


