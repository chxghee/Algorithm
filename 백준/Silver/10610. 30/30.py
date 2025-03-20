# https://www.acmicpc.net/problem/10610
# n < 100,000
import sys
input = sys.stdin.readline

# 일단 마지막 자리가 0 이 아니면 못만듬 -> 0을 제외하고 3의 배수만 찾으면 됨
# 3의 배수는 모든 자릿수 합이 3의 배수면 가능
def find_number(num):

    if num[-1] != '0':
        return -1
    
    if sum(map(int, num)) % 3 != 0:
        return -1
    
    st = "".join(num)
    return int(st)


n = int(input())
num = list(str(n))
num.sort(reverse=True)

print(find_number(num))
