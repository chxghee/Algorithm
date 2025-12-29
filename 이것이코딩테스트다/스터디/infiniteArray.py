# https://www.acmicpc.net/problem/33559
from collections import Counter
import sys
input = sys.stdin.readline

def print_array(array):
    for val in array:
        print(val, end=" ")
    print()

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
counter_a = Counter(a)
counter_b = Counter(b)

same = []
rest_a = []
rest_b = []

for val in set(a+b):
    same_number_cnt = min(counter_a[val], counter_b[val])
    same += [val] * same_number_cnt
    rest_a += [val] * (counter_a[val] - same_number_cnt)
    rest_b += [val] * (counter_b[val] - same_number_cnt)

print(len(same))
print_array(same + rest_a)
print_array(same + rest_b)


# 카운터 사용법
# Counter(리스트) 를 하면 리스트의 요소를 키로 하고 등장 횟수를 값으로 하는 딕셔너리 생성
# 가장 많이 나오는 순으로 정렬은 counter.most_common() 으로 정렬 가능
# 딕셔너리 순회
# for key, val in dict.items(): -> 키 값으로 순회
# for key in dict: -> 키 값으로 순회
# 키만 리스트로 -> list(dict.keys())