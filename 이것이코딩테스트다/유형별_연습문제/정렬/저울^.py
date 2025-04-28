# https://www.acmicpc.net/problem/2437
# 풀이 전략이 생각나지 않았던 문제

# 1. "항상 작은 것부터 다루는 게 안전할까?"  
# 2. 작은 것부터 검토해 본다면 현재까지의 데이터로 어디까지 할수 있을 지
# 고민해 보고 정렬 도입을 결정하자



import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

scala = 0
for weight in data:
    if weight > scala + 1:
        print(scala + 1)
        break
    scala += weight

else:
    print(scala + 1)

# for - else 문법: break 없이 끝까지 다 돌면 else 실행
