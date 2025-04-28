# https://www.acmicpc.net/problem/2108
from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())

avg = 0
data = []

for i in range(n):
    d = int(input())
    data.append(d)
    avg += d 

data.sort()


counter = Counter(data)         # 카운터로 빈도 한번에 세기 (딕셔너리)
freq = counter.most_common()    # 카운터를 리스트로 변환
max_freq = freq[0][1]

f = [val for val, frequency in freq if frequency == max_freq]
f.sort()

if len(f) == 1:
    fq = f[0]
else:
    fq = f[1]


avg = round(avg / n)

mean = data[n//2]

diff = data[n-1] - data[0]

print(avg)
print(mean)
print(fq)
print(diff)