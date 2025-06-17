import sys
input = sys.stdin.readline

n,m = map(int, input().split())
rice = list(map(int, input().split()))

start = 1
end = max(rice)

result = 0
while start <= end:

    mid = (start + end) // 2

    total = 0
    for r in rice:
        sub = r - mid
        if sub > 0:
            total += sub


    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1


print(result)