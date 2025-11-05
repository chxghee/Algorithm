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



