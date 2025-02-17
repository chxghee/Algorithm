import sys

n,m = map(int, sys.stdin.readline().split())
rice = list(map(int, sys.stdin.readline().split()))


# 젤 긴거 -1 부터 젤 긴거 - m 까지
end = max(rice)
start = 0

while start <= end:
    
    mid = (end + start) // 2
    result = 0
    for r in rice:
        sub = r - mid
        if sub > 0:
            result += sub
    
    if result == m:
        break
    elif result < m:
        end = mid - 1
    else:
        start = mid + 1

    

print(mid)



