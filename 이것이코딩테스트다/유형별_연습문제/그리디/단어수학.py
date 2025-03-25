# https://www.acmicpc.net/problem/1339
import sys
from collections import defaultdict     # 딕셔너리 초기화 용이

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    a = input().rstrip()
    data.append(list(a)) 


dic_alpha = defaultdict(int)
dic_result = defaultdict(int)

for i in range(n):
    st_len = len(data[i])
    for c in data[i]:
        dic_alpha[c] += 10 ** (st_len-1)
        st_len -= 1

# 딕셔너리 정렬
sorted_dic = dict(sorted(dic_alpha.items(), key=lambda x: x[1], reverse=True))

num = 9
for key, val in sorted_dic.items():
    dic_result[key] = num
    num -= 1

print(dic_result)

result = 0
for i in range(n):
    number = 0
    data_len = len(data[i]) - 1
    for c in data[i]:
        number += dic_result[c] * (10 ** data_len)
        data_len -= 1
    
    result += number

print(result)