# https://www.acmicpc.net/problem/17140
import sys
input = sys.stdin.readline

def sorting(arr):
    cnt = [0] * (max(arr) + 1) 
    
    for val in arr:
        if val == 0:
            continue

        cnt[val] += 1

    l = []    
    for i in range(len(cnt)):
        if cnt[i] != 0:
            l.append((cnt[i], i))
    l.sort()

    new_arr = []
    for val in l:
        new_arr.append(val[1])
        new_arr.append(val[0])
    
    return new_arr

def operation_r(r_idx):
    return sorting(a[r_idx])

def operation_c(c_idx):
    arr = [a[i][c_idx] for i in range(len(a))]
    return sorting(arr)


def append_row_arr(arr, idx):
    
    for i in range(len(arr)):
        new_a[idx][i] = arr[i]

def append_col_arr(arr, idx):

    for i in range(len(arr)):
        new_a[i][idx] = arr[i]


r,c,k = map(int, input().split())
r -= 1
c -= 1
a = [list(map(int, input().split())) for _ in range(3)]

r_max_len = 3
c_max_len = 3

t = 0
for i in range(101):

    if not (r >= r_max_len or c >= c_max_len) and a[r][c] == k:    
        break
    
    
    new_a = [[0] * 100 for _ in range(100)]

    # 열의 개수 <= 행의 개수 -> r 연산
    if c_max_len <= r_max_len:
        for r_idx in range(r_max_len):
            new_arr = operation_r(r_idx)
            c_max_len = max(c_max_len, len(new_arr))
            append_row_arr(new_arr, r_idx)            
    
    else:
        for c_idx in range(c_max_len):
            new_arr = operation_c(c_idx)
            r_max_len = max(r_max_len, len(new_arr))
            append_col_arr(new_arr, c_idx)

    a = new_a
    t += 1

if t == 101:
    t = -1

print(t)