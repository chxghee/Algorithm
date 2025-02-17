# https://www.acmicpc.net/problem/1715
# 시간초과 고려

import sys

n = int(sys.stdin.readline().rstrip())
num = [int(sys.stdin.readline().rstrip()) for _ in range(n)]


def my_sort(arr):

    count = [0] * (max(num) + 1)

    for i in range(len(num)):
        count[num[i]] += 1

    sorted_num = []
    for i in range(len(count)-1, -1, -1):
        for j in range(count[i]):
            sorted_num.append(i)

    return sorted_num


result = 0

while num:
    num = my_sort(num)     
    if len(num) >= 2:
        a = num.pop()
        b = num.pop()
    else:
        break

    x = a+b
    result += x
    num.append(x)
    
        
    


print(result)


