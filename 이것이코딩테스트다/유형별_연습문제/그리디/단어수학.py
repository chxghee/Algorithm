# https://www.acmicpc.net/problem/1339
import sys
from collections import defaultdict     # 딕셔너리 초기화

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(input().rstrip())) 

# 뭐가 들어올지 모르는 상황에서 해당 값을 키로 놓고 횟수를 증가시킬 수 잇따.
dic_alpha = defaultdict(int)    # 각 자리수를 고려해서 정량적으로 해당 알파벳 크기를 측정
dic_result = defaultdict(int)   # 해당 알파벳을 치환 할 숫자 지정

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

result = 0
for i in range(n):
    number = 0
    data_len = len(data[i]) - 1
    for c in data[i]:
        number += dic_result[c] * (10 ** data_len)
        data_len -= 1
    
    result += number

print(result)