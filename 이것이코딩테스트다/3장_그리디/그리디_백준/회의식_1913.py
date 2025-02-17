# https://www.acmicpc.net/problem/1931

n = int(input())

meetings = []
for i in range(n):
    t = list(map(int, input().split()))
    meetings.append(t)

meetings.sort(key=lambda x: (x[1], x[0]))

# 1. 가장 먼저 끝나는 거 선택
i = 0
end = 0
count = 0
while i<n:

    if end <= meetings[i][0]:
        end = meetings[i][1]
        count += 1
    
    i += 1

print(count)

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

4
1 4
2 3
3 5
4 6

5
1 5
1 5
1 5
1 5
1 5

6
1 10
2 3
4 4
4 5
5 6
7 8

"""